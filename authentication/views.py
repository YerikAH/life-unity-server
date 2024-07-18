from rest_framework.exceptions import ValidationError
from .models import UserModel
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Llama al método create original de ModelViewSet
            response = super(UserViewSet, self).create(
                request, *args, **kwargs)
            return response
        except ValidationError as e:
            return Response({'error': 'No se puede crear el usuario', "content": str(e)}, status=status.HTTP_400_BAD_REQUEST)
