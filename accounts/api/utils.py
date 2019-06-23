import datetime
from django.utils import timezone
from django.conf import settings
from rest_framework.reverse import reverse as api_reverse

expires = settings.JWT_AUTH["JWT_EXPIRATION_DELTA"]

def jwt_access_response_payload_handler(token,user=None,request=None):
	return {

	"Your Token" : token,
	"Your username" : user.username,
	"Your Token will expire on": (timezone.now() + expires - datetime.timedelta(seconds = 200)).strftime("%d/%m/%Y, %H:%M:%S"),
	"Refresh Your Token at" :  api_reverse("api_token:refresh",request = request)
	}



response_expires = settings.JWT_AUTH["JWT_REFRESH_EXPIRATION_DELTA"]

def jwt_response_payload_handler(token,user=None,request=None):
	return {

	"Your new Token" : token,
	"Your username" : user.username,
	"Your Token will expire on": (timezone.now() + response_expires - datetime.timedelta(seconds = 200)).strftime("%d/%m/%Y, %H:%M:%S")
	}
