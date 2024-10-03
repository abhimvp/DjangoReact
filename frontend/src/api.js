// # here i'm going to write something known as interceptor.
// # interceptor will essentially intercept any request that we're going to send and it will automatically add the correct headers
// # so that we don't need to manually write it a bunch of difff. times repetitively in our code
// # here we're going to use AXIOS - really clean way too send network requests - easy to use
// # here we're going to setup axios interceptor - where anytime we send a request it's gng to check if we have an access token
// # & if we do it will automatically add it to that request

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // import anything that's specified inside an environment variable file - url to backend server
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; // this is how we pass jwt access token
      // create an Authorization header - automaticlly handled by axios
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
//  from now on we're going to use this api object rather than using axios by default to send all diff requests
// so that authorization token will automatically be added
