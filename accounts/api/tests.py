from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase


from django.contrib.auth.models import User


class UserAPITestCase(APITestCase):

	def setUp(self): 
		user =  User.objects.create(username='ubaid123', email='hello@ubaid.com')
		user.set_password(".ubaid111")
		user.save()

	def test_created_user(self):
		qs = User.objects.filter(username='ubaid123')
		self.assertEqual(qs.count(), 1)

	def test_register_user_api(self):
		url = api_reverse('api_token:register')
		data = {
			'username': 'john-doe',
			'email': 'john-doe@gmail.com',
			'password': 'learncode',
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED) # 400
		token_len = len(response.data.get("token", 0))
		self.assertGreater(token_len, 0)# 400



	def test_login_user_api(self):
		url = api_reverse('api_token:auth')
		data = {
			'username': 'ubaid123',
			'password': '.ubaid111',
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK) # 400
		token = response.data.get("Your Token", 0)
		token_len = 0
		if token != 0:
			token_len = len(token)
		self.assertGreater(token_len, 0)



	def test_login_user_api_fail(self):
		url = api_reverse('api_token:auth')
		data = {
			'username': 'john-doe2',
			'password': 'learncode',
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) # 400
		token = response.data.get("token", 0)
		token_len = 0
		if token != 0:
			token_len = len(token)
		self.assertEqual(token_len, 0)
	
	def test_token_login_api(self):
		url = api_reverse('api_token:auth')
		data = {
			'username': 'ubaid123',
			'password': '.ubaid111',
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK) #400
		token = response.data.get("Your Token", None)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		response2 = self.client.post(url, data, format='json')
		self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)


	def test_token_register_api(self):
		url = api_reverse('api_token:auth')
		data = {
			'username': 'ubaid123',
			'password': '.ubaid111',
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK) #400
		token = response.data.get("Your Token", None)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

		url2 = api_reverse('api_token:register')
		data2 = {
			'username': 'john-doe3',
			'email': 'john-doe3@gmail.com',
			'password': 'learncode',
			'password2': 'learncode'
		}
		response = self.client.post(url2, data2, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # 403
