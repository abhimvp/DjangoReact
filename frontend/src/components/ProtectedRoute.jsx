// this represents as a wrapper for a protected route
// The idea is if we wrap something in protected route , then we need to have an authorization token before we'll be able to
// access this route
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useState, useEffect } from "react";
// custom frontend protection code
function ProtectedRoute({ children }) {
  // children is a prop that represents the component that we want to protect/wrap
  const [isAuthorized, setIsAuthorized] = useState(null);

  useEffect(() => {
    auth().catch(() => setIsAuthorized(false));
  }, []);
  const refreshToken = async () => {
    // refresh the access token for us automatically
    const refreshToken = localStorage.getItem(REFRESH_TOKEN);
    try {
      // send a request to my backend with my refresh token to get a new access token
      const res = await api.post("api/token/refresh/", {
        refresh: refreshToken,
      });
      if (res.status === 200) {
        const { access } = res.data;
        localStorage.setItem(ACCESS_TOKEN, access);
        setIsAuthorized(true);
      } else {
        setIsAuthorized(false);
      }
    } catch (err) {
      console.log(err);
      setIsAuthorized(false);
    }
  };

  const auth = async () => {
    // checks is we need to refresh the token or not
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      setIsAuthorized(false);
      return;
    }
    const decoded = jwtDecode(token);
    const tokenExpiration = decoded.exp;
    const now = Date.now() / 1000; // get date in seconds

    if (tokenExpiration < now) {
      await refreshToken();
    } else {
      setIsAuthorized(true);
    }
  };

  if (isAuthorized === null) {
    return <div> Loading ... </div>;
  }

  return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
