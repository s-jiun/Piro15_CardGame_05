from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import PositiveIntegerField


class Card(models.Model):
    value = PositiveIntegerField() #random

class User(AbstractUser):
    name = models.CharField(max_length=50)
    record = models.CharField(max_length=50) #전적?
    selected_card = models.ForeignKey(Card, on_delete=models.CASCADE) #선택한 카드
    result = models.CharField(max_length=10) #경기 결과 승/패
    score = models.IntegerField()
    rank = models.PositiveIntegerField() #전체 랭킹
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

