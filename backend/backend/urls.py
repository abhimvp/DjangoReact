"""
Here we configure all of our different urls , so that we can link them up & go to correct route
"""
from django.contrib import admin
from django.urls import path , include
from api.views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # prebuilt views that allow us to obtain our access and refresh tokens
    TokenRefreshView,
)

# these paths are urls we can go to , that will call a specific functiion or do some type of operation
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register'), # we are mapping our view to a url pattern
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'), # this is for login - frontend stores this
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/',include("rest_framework.urls")),
    path('api/',include("api.urls")),
]
