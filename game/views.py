
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

def main(request):
    return render(request, "game/main.html")

def game_attack(request, pk):
    if request.method == "POST":
        form = CardGameForm(request.POST)
        if form.is_valid():
            result = form.save()
            return redirect('game:game_result')
        #random_list = User.objects.get(id=pk).random_card_num()
    else:
        form = CardGameForm()
        random_list = random.sample(range(1, 11), 5)
        counters = User.objects.all()
        # ctx = {
        #     'random_list': random_list,
        #     'counters' : counters,
        # }
    return render(request, "game/attack.html", {'random_list': random_list,
            'counters' : counters, 'form': form,})


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

