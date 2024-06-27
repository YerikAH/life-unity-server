from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)