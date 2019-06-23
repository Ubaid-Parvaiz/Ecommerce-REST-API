from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

from buyer.api.serializers import Buyer_Inline_Serializer



class User_Public_Serializers(serializers.ModelSerializer):

	buyer = serializers.SerializerMethodField(read_only =True)
	
	class Meta:
		model = User
		fields = [
		"username",
		"email",
		"id",
		"buyer"
		]

	

	def get_buyer(self,obj):
		request = self.context.get("request")
		limit = 10
		if request:
			limit_query = request.GET.get("limit")
			try:
				limit = int(limit_query)
			except:
				pass	

		qs  = obj.buyer_set.all().order_by('-created')
		qs2 = obj.buyer_set.latest("id")

		data = {
		 "latest"  : Buyer_Inline_Serializer(qs2,context = {"request": request}).data,
		 "recent": Buyer_Inline_Serializer(qs[:limit],many=True,context = {"request": request}).data,

		}
		return data




