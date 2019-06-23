from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.parsers import JSONParser


from .utils import jwt_response_payload_handler,jwt_access_response_payload_handler


from rest_framework_jwt.settings import api_settings

from .serializers import UserForm_Serializers,User_Register

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER

from django.contrib.auth import authenticate

from .permissions import Allow_UA

from rest_framework import mixins

from rest_framework import generics

class AuthAPIView(APIView):
	serializer_class = UserForm_Serializers

	def get(self,request,*agrs,**kwargs):

			#print(request.user)
		if request.user.is_authenticated():
			user = request.user
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
			response = jwt_response_payload_handler(token, user, request=request)
			return Response(response)
		return Response("You are not authenticated please authenticate your-self first.")	
		
		
	def post(self, request, *args, **kwargs):
		#print(request.user)
		if request.user.is_authenticated():
			return Response({'detail': 'You are already authenticated'}, status=400)

		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username = username,password=password)

			if user:
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				response = jwt_access_response_payload_handler(token, user, request=request)
				return Response(response)
		return Response({"detail": "Invalid credentials"}, status=401)



class User_Register_View(generics.CreateAPIView):
	serializer_class   = User_Register 
	permission_classes = [Allow_UA]


	def get_serializer_context(self,*args,**kwargs):
		return {"request":self.request}

