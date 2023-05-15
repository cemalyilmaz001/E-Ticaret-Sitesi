from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("mybasket/", views.mybasket, name="mybasket"),
    path("abonelik_save/", views.email_abonelik, name="email_abonelik"),
]
