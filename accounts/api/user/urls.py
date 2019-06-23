from django.conf.urls import url

from . import views


urlpatterns = [

url(r"^(?P<username>[\w.@+-]+)/$",views.User_Public_View.as_view(),name = "user")\


]