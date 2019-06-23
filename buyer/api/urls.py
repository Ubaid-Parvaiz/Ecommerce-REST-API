from django.conf.urls import url

from . import views

urlpatterns = [



url(r'^list/$',views.BuyerList.as_view(),name = "buyer_list"),
url(r'^list/(?P<id>\d+)/$',views.BuyerDetail.as_view(),name = "buyer_detail")





]