from buyer.models import Buyer 

from rest_framework import serializers 

from rest_framework.reverse import reverse as api_reverse

from . import views 

from accounts.api.serializers import User_Serializers

class Buyer_Serializer(serializers.ModelSerializer):
	# uri = serializers.HyperlinkedRelatedField(

	# 										source = "Buyer",
	# 										read_only = True,
	# 										view_name = "api:buyer_detail"


	# 										)


	User_Details = serializers.SerializerMethodField()
	uri  = serializers.SerializerMethodField(read_only =True)
	class Meta:
		model = Buyer
		fields = [
		"User_Details",
		"user",
		"order",
		"created",
		"updated",
		"uri",
		"order_image",
		"id",


		]

	def get_uri(self,obj):
		request = self.context.get('request')	
		return api_reverse("api:buyer_detail",kwargs = {"id":obj.id},request = request)

	
	def get_User_Details(self,obj):
		request = self.context.get("request")
		print(obj)
		qs  = obj.user

		data = {
		 "user"  : User_Serializers(qs,context = {"request": request}).data,

		}
		return data		





class Buyer_Inline_Serializer(serializers.ModelSerializer):
	# uri = serializers.HyperlinkedRelatedField(

	# 										source = "Buyer",
	# 										read_only = True,
	# 										view_name = "api:buyer_detail"


	# 										)


	uri  = serializers.SerializerMethodField(read_only =True)
	class Meta:
		model = Buyer
		fields = [
		"id",
		"order",
		"created",
		"updated",
		"uri",
		"order_image"


		]

	def get_uri(self,obj):
		request = self.context.get("request")
		return api_reverse("api:buyer_detail",kwargs = {"id":obj.id},request = request)

