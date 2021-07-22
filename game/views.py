from django.shortcuts import render
from .models import CardGame

# Create your views here.
def game_info(request, pk):
    info = CardGame.objects.get(id=pk)
    ctx = {'info': info}
    return render(request, 'game/info.html', context=ctx)

def game_result(request):
    results = CardGame.objects.all()
    ctx = {'results': results}
    return render(request, 'game/result.html', context=ctx)