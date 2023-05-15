from django.shortcuts import render
from django.shortcuts import redirect
from .models import Site_Ayarları, Slide_Gösterisi, Email_Abonelik, Ürün_Listesi

site  = Site_Ayarları.objects.all()
slide = Slide_Gösterisi.objects.all()
ürün_list = Ürün_Listesi.objects.all()

# Create your views here.
def index(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "base.html",context)

def login(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "login.html",context)

def register(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "register.html",context)

def mybasket(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "basket.html",context)

def email_abonelik(request):
    if request.method == 'POST':
        abone = request.POST["email_abonelik"]
        email = Email_Abonelik.objects.create(email_address=abone)
        email.save()
        return redirect("/")
    else:
        return redirect("/")