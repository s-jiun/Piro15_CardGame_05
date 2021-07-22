
from django.shortcuts import render, redirect
from .models import CardGame, User
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "game/login.html", context=ctx)

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

