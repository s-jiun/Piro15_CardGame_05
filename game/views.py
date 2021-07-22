from django.shortcuts import render
from .models import CardGame

# Create your views here.
def game_info(request, pk):
    info = CardGame.objects.get(id=pk)
    ctx = {'info': info}
    return render(request, 'game/info.html', context=ctx)
    