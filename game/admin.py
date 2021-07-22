from django.contrib import admin
from .models import CardGame

# Register your models here.
@admin.register(CardGame)
class CardGameAdmin(admin.ModelAdmin):
    pass