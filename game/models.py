from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from random import randint

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)

    score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class CardGame(models.Model):
    MORE = '숫자가 더 큰 사람'
    LESS = '숫자가 더 적은 사람'

    RULE_CHOICES = (
        (MORE, '숫자가 더 큰 사람'),
        (LESS, '숫자가 더 적은 사람')
    )

    host = models.ForeignKey(User, on_delete=CASCADE, related_name='game_host')
    guest = models.ForeignKey(User, on_delete=CASCADE, related_name='game_guest')

    host_card = models.PositiveIntegerField(default=0)
    guest_card = models.PositiveIntegerField(default=0)

    rule = models.CharField(max_length=50, choices=RULE_CHOICES )

    result = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

