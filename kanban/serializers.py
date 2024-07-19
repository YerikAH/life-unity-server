from rest_framework.serializers import ModelSerializer
from .models import Board, Cards, SubCard

class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class CardSerializer(ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'

class SubCardSerializer(ModelSerializer):
    class Meta:
        model = SubCard
        fields = '__all__'