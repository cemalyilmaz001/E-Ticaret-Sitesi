from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("abonelik_save/", views.email_abonelik, name="email_abonelik"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("mybasket/", views.mybasket, name="mybasket"),
]
