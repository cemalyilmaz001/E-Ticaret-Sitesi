from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("my/", views.bzkmz, name="bzkmz"),
    path("questions/", views.soru, name="soru"),

    path("abonelik_save/", views.email_abonelik, name="email_abonelik"),
    path("contact/", views.contact, name="contact"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("myprofil/", views.myprofil, name="myprofil"),
    path("mybasket/", views.mybasket, name="mybasket"),
    path("setting/", views.ayarlar, name="setting"),
]
