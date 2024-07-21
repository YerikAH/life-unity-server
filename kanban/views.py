from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Board, SubCard, Cards
from .serializers import BoardSerializer, CardSerializer, SubCardSerializer

# Create your views here.
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

class CardViewSet(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class SubCardViewSet(ModelViewSet):
    queryset = SubCard.objects.all()
    serializer_class = SubCardSerializer
    permission_classes = [IsAuthenticated]