from django.db import models
from django.db.models.enums import Choices
from random import randint

# Create your models here.
class CardGame(models.Model):
    WIN = '승리'
    LOSE = '패배'
    DRAW = '무승부'

    RESULT_CHOICES = (
        (WIN, '승리'),
        (LOSE, '패배'),
        (DRAW, '무승부'),
        )

    MORE = '숫자가 더 큰 사람'
    LESS = '숫자가 더 적은 사람'

    RULE_CHOICES = (
        (MORE, '숫자가 더 큰 사람'),
        (LESS, '숫자가 더 적은 사람')
    )

    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)

    player1_card = models.PositiveIntegerField(randint(1,10))
    player2_card = models.PositiveIntegerField(randint(1,10))

    rule = models.CharField(max_length=50, choices=RULE_CHOICES )

    result = models.CharField(max_length=50, choices=RESULT_CHOICES)

    my_score = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)