from rest_framework.serializers import ModelSerializer
from .models import UserModel
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    # el cliente solo puede enviar mas no recibir
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {
            'username':  {'required': True},
            'email':  {'required': True},
            'password':  {'required': True},
            'first_name':  {'required': True},
            'last_name':  {'required': True},
        }
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        # Si estamos actualizando (self.instance no es None), hacemos ciertos campos no requeridos
        # self.instance -> instancia del objeto que se está serializando o deserializando
        if self.instance is not None:
            self.fields['password'].required = False
            self.fields['first_name'].required = False
            self.fields['last_name'].required = False
            self.fields['email'].required = False
            # Puedes hacer opcional cualquier otro campo necesario

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data.get('password'))
        return super().update(instance, validated_data)

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
    
