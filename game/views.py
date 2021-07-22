from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout

def main(request):
    return render(request, "game/main.html")

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
