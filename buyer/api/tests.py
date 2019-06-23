import shutil
import os
import io
from PIL import Image

from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework_jwt.settings import api_settings

from buyer.models import Buyer

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class BuyerAPITestCase(APITestCase): 
	def setUp(self): 
		user =  User.objects.create(username='ubaid123', email='hello@ubaid.com')
		user.set_password(".ubaid111")
		user.save()
		Buyer_obj = Buyer.objects.create(user=user, order='Blue jeans jacket!')

	def test_statuses(self):
		self.assertEqual(Buyer.objects.count(), 1)


	def status_user_token(self):
		auth_url = api_reverse('api_token:auth')
		auth_data = {
			'username': 'ubaid123',
			'password': '.ubaid111',
		}
		auth_response = self.client.post(auth_url, auth_data)
		token = auth_response.data.get("Your Token", None)
		if token is not None:
			self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

	def create_item(self):
		self.status_user_token()
		url = api_reverse('api:buyer_list')
		data = {
			'user':1,
			'order': "some cool test content",
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Buyer.objects.count(), 2)
		return response.data

	def test_empty_create_item(self):
		self.status_user_token()
		url = api_reverse('api:buyer_list')
		data = {
			'order': None,
			'order_image': None
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		return response.data

	def generate_photo_file(self):
		file = io.BytesIO()
		image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
		image.save(file, 'png')
		file.name = 'test.png'
		file.seek(0)
		return file

	def test_upload_photo(self):
		self.status_user_token()

		"""
		Test if we can upload a photo
		"""


		url = reverse('api:buyer_list')

		photo_file = self.generate_photo_file()

		data = {
				'user':1,
				'order':"image test",
				'order_image':photo_file
			}

		response = self.client.post(url, data, format='multipart')
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Buyer.objects.count(), 2)
		temp_img_dir = os.path.join(settings.MEDIA_ROOT,  )
		if os.path.exists(temp_img_dir):
			shutil.rmtree(temp_img_dir)



	def test_status_create(self):
	    data = self.create_item()
	    data_id = data.get("id")
	    data_user = data.get("user")

	    rud_url = api_reverse('api:buyer_detail', kwargs={"id": data_id})
	    rud_data = {
	   		 "user" : data_user,
	        'order': "another new content"
	    }

	    '''
	    get method / retrieve
	    '''
	    get_response = self.client.get(rud_url, format='json')
	    self.assertEqual(get_response.status_code, status.HTTP_200_OK)

	def test_status_update(self):
	    data = self.create_item()
	    data_user = data.get("user")
	    data_id = data.get("id")
	    rud_url = api_reverse('api:buyer_detail', kwargs={"id": data_id})
	    rud_data = {
	    	"user" : data_user,
	        'order': "another new content"
	    }
	    '''
	    put / update
	    '''
	    put_response = self.client.put(rud_url, rud_data, format='json')
	    self.assertEqual(put_response.status_code, status.HTTP_200_OK)
	    rud_response_data = put_response.data
	    self.assertEqual(rud_response_data['order'], rud_data['order'])
		
	def test_status_delete(self):
	    data = self.create_item()
	    data_user = data.get("user")
	    data_id = data.get("id")
	    rud_url = api_reverse('api:buyer_detail', kwargs={"id": data_id})
	    rud_data = {
	    	"user" : data_user,
	        'order': "another new content"
	    }
	    '''
	    delete method / delete
	    '''
	    del_response = self.client.delete(rud_url, format='json')
	    self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
	    '''
	    Not found
	    '''
	    get_response = self.client.get(rud_url, format='json')
	    self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


	def test_status_no_token_create(self):
		url = api_reverse('api:buyer_list')
		data = {

			'order': "some cool test content"
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_other_user_permissions_api(self):
	    data            = self.create_item()
	    data_id         = data.get("id")
	    user            = User.objects.create(username='testjmitch')
	    payload         = jwt_payload_handler(user)
	    token           = jwt_encode_handler(payload)
	    self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
	    rud_url         = api_reverse('api:buyer_detail', kwargs={"id": data_id})
	    rud_data        = {
	                        'order': "smashing"
	                    }
	    get_            = self.client.get(rud_url, format='json')
	    put_            = self.client.put(rud_url, rud_data, format='json')
	    delete_         = self.client.delete(rud_url, format='json')
	    self.assertEqual(get_.status_code, status.HTTP_200_OK)
	    self.assertEqual(put_.status_code, status.HTTP_401_UNAUTHORIZED)
	    self.assertEqual(delete_.status_code, status.HTTP_401_UNAUTHORIZED)