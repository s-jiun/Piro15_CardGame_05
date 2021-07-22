from django.contrib import admin
from .models import CardGame, User

# Register your models here.
@admin.register(CardGame)
class CardGameAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass