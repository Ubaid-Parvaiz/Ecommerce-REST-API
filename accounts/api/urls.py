from rest_framework_jwt.views import refresh_jwt_token,verify_jwt_token
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^auth/$', views.AuthAPIView.as_view(),name = "auth"),

    url(r'^refresh/$', refresh_jwt_token,name = "refresh"),

    url(r'^verify/$', verify_jwt_token,name = "verify"),

    url(r"^register/$",views.User_Register_View.as_view(),name = "register")




]