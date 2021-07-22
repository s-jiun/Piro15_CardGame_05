from django.shortcuts import render
from .models import CardGame, User

# Create your views here.
def game_info(request, pk):
    info = CardGame.objects.get(id=pk)
    ctx = {'info': info}
    return render(request, 'game/info.html', context=ctx)

def game_result(request):
    results = CardGame.objects.all()
    ctx = {'results': results}
    return render(request, 'game/result.html', context=ctx)

def game_podium(request):
# 점수에 따라 ordering하여 가져옴
    users  = User.objects.all()
    ctx = {'users': users}
    return render(request, 'game/game_podium.html', context=ctx)