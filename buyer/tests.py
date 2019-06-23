from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Buyer

User = get_user_model()


class StatusTestCase(TestCase): 
	def setUp(self): 
		user =  User.objects.create(username='ubaid', email='hello@ubaid.com')
		user.set_password(".ubaid")
		user.save()

	def test_creating_status(self):
		user = User.objects.get(username='ubaid')
		obj = Buyer.objects.create(user=user, order='Some cool new content')
		self.assertEqual(obj.id, 1)
		qs = Buyer.objects.all()
		self.assertEqual(qs.count(), 1)