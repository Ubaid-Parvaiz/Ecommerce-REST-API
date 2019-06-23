from rest_framework import generics

from .serializers import User_Public_Serializers

from rest_framework import permissions

from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Q

from rest_framework.response import Response

import json

from rest_framework import status

from rest_framework.views import APIView

class User_Public_View(generics.ListAPIView):
	serializer_class = User_Public_Serializers
	queryset 	     = User.objects.filter(is_active = True)
	permission_class = [permissions.IsAuthenticatedOrReadOnly]

	
	def get_queryset(self):
		"""
		This view should return a list of the  user as determined by the username portion of the URL.
		
		"""
		username = self.kwargs['username']
		return User.objects.filter(username=username)



# class User_Public_View(APIView):
# 	permission_class = [permissions.IsAuthenticatedOrReadOnly]

# 	def get(self,request,*args,**kwargs):
# 		qs   		 = User.objects.filter(


# 			Q(is_active =True),
# 			Q(username = self.kwargs.get("username"))

# 		) 
# 		print(self.kwargs.get("username"))

# 		serializer = User_Public_Serializers(qs,many=True)
# 		return Response(serializer.data)




