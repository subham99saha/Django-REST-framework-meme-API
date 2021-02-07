from rest_framework import serializers
from api.models import *

class memeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meme
		fields = "__all__"