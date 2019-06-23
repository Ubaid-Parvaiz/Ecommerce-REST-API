import datetime

from django.utils import timezone

from rest_framework import serializers 

from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.response import Response


from .utils import jwt_access_response_payload_handler

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER

from django.conf import settings

expires = settings.JWT_AUTH["JWT_EXPIRATION_DELTA"]



class User_Serializers(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model  = User
		fields = [
		
			"id",
			"username",
			"email"


		] 


class UserForm_Serializers(serializers.ModelSerializer):
	

	class Meta:
		model  = User
		fields = [

			"username",
			"password",

		] 
	





class User_Register(serializers.ModelSerializer):
	token   = serializers.SerializerMethodField(read_only =True)
	expires = serializers.SerializerMethodField(read_only =True) 
	
	class Meta:
		model  = User
		fields = [

		"username",
		"email",
		"password",
		"token",
		"expires"


		]	

	def get_token(self,obj):
		request = self.context.get("request")
		payload = jwt_payload_handler(obj)
		token = jwt_encode_handler(payload)
		return token

	
	def get_expires(self,obj):
		return (timezone.now() + expires - datetime.timedelta(seconds = 200)).strftime("%d/%m/%Y, %H:%M:%S")
