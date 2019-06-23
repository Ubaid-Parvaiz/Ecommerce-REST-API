from rest_framework import generics

from rest_framework import mixins

from rest_framework import permissions
from rest_framework.response import Response

from . import serializers

from buyer.models import Buyer 

class BuyerList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class   = serializers.Buyer_Serializer
	queryset   		   = Buyer.objects.all()
	ordering_fields = ('username', 'email',"created")
	search_fields =  ('user__username',"user__email")




class BuyerDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class = serializers.Buyer_Serializer
	queryset   		 = Buyer
	lookup_field   = "id"


