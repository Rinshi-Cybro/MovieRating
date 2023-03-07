from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
    path('user',UserView.as_view()),
    path('token',obtain_auth_token)
    ]
