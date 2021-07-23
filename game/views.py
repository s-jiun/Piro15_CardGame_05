
from django.shortcuts import render, redirect
from .models import CardGame, User
from django.views import View
from .forms import UserForm, CardGameForm
from . import forms
from django.contrib.auth import authenticate, login, logout
import random
from django.http import HttpResponse


# Create your views here.
def game_info(request, pk):
    game = CardGame.objects.get(id=pk)
    ctx = {'game': game}
    return render(request, 'game/info.html', context=ctx)


def game_result(request):
    results = CardGame.objects.filter(
        host=request.user) | CardGame.objects.filter(guest=request.user)
    ctx = {'results': results}
    return render(request, 'game/result.html', context=ctx)


def game_podium(request):
    # 점수에 따라 ordering하여 가져옴
    users = User.objects.all().order_by('-score')

    players = User.objects.count() #유저 개수

    i = 1
    for user in users:
        user.rank = i
        i += 1
    
    ctx = {'users': users,
    "players": players,
        }
    return render(request, 'game/game_podium.html', context=ctx)


def main(request):
    return render(request, "game/main.html")


def game_attack(request):
    if request.method == "POST":
        CardGame(host=request.user, guest=User.objects.get(
            username=request.POST['picked_cp']), host_card=request.POST['picked_card']).save()

        return redirect('game:game_result')
        #random_list = User.objects.get(id=pk).random_card_num()
    else:
        random_list = random.sample(range(1, 11), 5)
        counters = User.objects.exclude(username=request.user.username)
        # ctx = {
        #     'random_list': random_list,
        #     'counters' : counters,
        # }
    return render(request, "game/attack.html", {'random_list': random_list,
                                                'counters': counters, })


def game_counterattack(request, pk):
    if request.method == "POST":
        game = CardGame.objects.get(id=pk)
        g_card = request.POST['picked_card']

        rules = ['more', 'less']
        rand_rule = random.choice(rules)
        game.rule = rand_rule
        game.is_end = True
        h_card = int(game.host_card)
        g_card = int(game.guest_card)
        if rand_rule == 'more':
            if h_card > g_card:
                game.result = 'win'

            elif h_card == g_card:
                game.result = 'draw'
            else:
                game.result = 'lose'
        else:
            if h_card < g_card:
                game.result = 'win'
            elif h_card == g_card:
                game.result = 'draw'
            else:
                game.result = 'lose'
        if game.result == 'win':
            game.host.score += h_card
            game.guest.score -= g_card

        elif game.result == 'lose':
            game.host.score -= h_card
            game.guest.score += g_card

        game.host.save()
        game.guest.save()
        game.save()

        return redirect('game:game_result')
        #random_list = User.objects.get(id=pk).random_card_num()
    else:
        random_list = random.sample(range(1, 11), 5)
        # ctx = {
        #     'random_list': random_list,
        #     'counters' : counters,
        # }
    return render(request, "game/counterattack.html", {'random_list': random_list, })


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "game/login.html", ctx)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            # cleaned_data = {'email': email@dfksldf.com, 'password': 1234}
            if user is not None:
                login(request, user)
                return render(request, "game/success.html")

        return render(request, "game/login.html", {"form": form})


def log_out(request):
    logout(request)
    return render(request, "game/main.html")
