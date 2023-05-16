from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

def email_abonelik(request):
    if request.method == 'POST':
        abone = request.POST["email_abonelik"]
        email = Email_Abonelik.objects.create(email_address=abone)
        email.save()
        return redirect("/")
    else:
        return redirect("/")

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

def login_view(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f' Hoşgeldiniz {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'Hatalı Giriş Yaptınız !')
    else:
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

    if request.method == 'POST':
        email           = request.POST['email']
        username        = request.POST['username']
        password        = request.POST['password']
        password_tekrar = request.POST['passwordx']
        for user in User.objects.all():
            if user.username == username:
                messages.success(request, f' Kullanıcı adınız kullanılmakta !!')
                return redirect('/register')

        if password == password_tekrar:
            user = User.objects.create_user(f"{str(username)}", f"{str(email)}", f"{str(password)}")
            user.save()
            messages.success(request, f' Kulllanıcı Kaydınız Oluşturuldu !!')
            return redirect('/login')
        else:
            messages.success(request, f' Parola Yanlış !!')
            return redirect('/register')
    else:
        context = {
            'site': site,
            'slide':slide,
            'ürün_list':ürün_list,
        }
        return render(request, "register.html",context)

def logout_view(request):
    logout(request)
    return redirect('/')
