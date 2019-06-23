from django.db import models
from django.contrib.auth.models import User


# Create your models here.

import os

def get_image_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

class Buyer(models.Model):
	user    = models.ForeignKey(User)
	order   = models.CharField(max_length = 210)
	order_image = models.ImageField(upload_to = get_image_path,blank = True, null =True)
	created = models.DateTimeField(auto_now_add = True)
	updated  = models.DateTimeField(auto_now = True)



	class Meta:
		verbose_name = "Buyer"
		verbose_name_plural = "Buyer Orders"

	
	def __str__(self):
		return self.order	
