from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    # main
    path("", views.main, name="main"),
    # # login
    path("login/", views.LoginView.as_view(), name="login"),
    # # logout
    path("logout/", views.log_out, name="logout"),
]
