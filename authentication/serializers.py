from rest_framework.serializers import ModelSerializer
from .models import UserModel
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__" 

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)
    
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)