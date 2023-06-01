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
    path("create_sepet/", views.create_sepet, name="create_sepet"),
    path("sepet_delete/", views.sepet_delete, name="sepet_delete"),
    path("sepet_eksi/", views.sepet_eksi, name="sepet_eksi"),
    path("sepet_arti/", views.sepet_arti, name="sepet_arti"),
    path("imageUpdate/", views.imageUpdate, name="imageUpdate"),
    path("hesap_guncelleme/", views.hesap_guncelleme, name="hesap_guncelleme"),
]