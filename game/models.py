from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser
from random import randint
import random

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    rank = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CardGame(models.Model):

    host = models.ForeignKey(User, on_delete=CASCADE, related_name='game_host')
    guest = models.ForeignKey(User, on_delete=CASCADE, related_name='game_guest')

    host_card = models.PositiveIntegerField(default=0)
    guest_card = models.PositiveIntegerField(default=0)

    is_end = models.BooleanField(default=False)

    rule = models.CharField(max_length=50, blank=True)

    result = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

