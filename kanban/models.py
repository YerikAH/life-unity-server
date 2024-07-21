from django.db import models
from authentication.models import UserModel


# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=100, null=False, blank=False)
    board_description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=100)
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, name='id_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'boards'

    def __str__(self):
        return self.board_name

class Cards(models.Model):
    card_name = models.CharField(max_length=100, null=False, blank=False)
    card_description = models.TextField(null=True, blank=True)
    position = models.IntegerField(null=False, default=1)
    vencimiento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=[
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Done', 'Done'),
    ])
    id_board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False, name='id_board')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cards'

    def __str__(self):
        return self.card_name

class SubCard(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    id_cards = models.ForeignKey(Cards, on_delete=models.CASCADE, null=False, name='id_cards')

    class Meta:
        db_table = 'sub_cards'

    def __str__(self):
        return self.name