from django.test import TestCase


from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase): 
    def setUp(self): 
        user =  User.objects.create(username='ubaid', email='hello@ubaid.com')
        user.set_password(".ubaid")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='ubaid')
        self.assertEqual(qs.count(), 1)