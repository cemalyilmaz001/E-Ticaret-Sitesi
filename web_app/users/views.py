from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Site_Ayarları, Slide_Gösterisi, Email_Abonelik, Ürün_Listesi, İletişim, kkb_hesabim, Yardım

site        = Site_Ayarları.objects.all()
slide       = Slide_Gösterisi.objects.all()
ürün_list   = Ürün_Listesi.objects.all()
kkb_hesap   = kkb_hesabim.objects.all()
ssss        = Yardım.objects.all()

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

def bzkmz(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "bzkm.html",context)

def soru(request):
    global site
    global slide
    global ürün_list
    global soru

    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
        'yardim':ssss,
    }
    return render(request, "sorular.html", context)

def email_abonelik(request):
    if request.method == 'POST':
        abone = request.POST["email_abonelik"]
        email = Email_Abonelik.objects.create(email_address=abone)
        email.save()
        messages.success(request, f'Kayıt Başarılı !!')
        return redirect("/")
    else:
        return redirect("/")

def contact(request):
    global site
    global slide
    global ürün_list

    if request.method == 'POST':
        email = request.POST["email"]
        user = request.POST["username"]
        istek = request.POST["isteks"]
        contact = İletişim.objects.create(email=email, ad=user, istek=istek)
        contact.save()
        messages.success(request, f'Kayıt Başarılı !!')
        return redirect("/")
    else:
        context = {
            'site': site,
            'slide':slide,
            'ürün_list':ürün_list,
        }
        return render(request, "iletişim.html",context)

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

def myprofil(request):
    global site
    global slide
    global ürün_list

    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
    }
    return render(request, "myprofil.html", context)

def imageUpdate(request):  
    global site
    global slide
    global ürün_list

    if request.FILES["image_update"] and request.POST["name"]:
        image = request.FILES["image_update"]
        name  = request.POST["name"]

        messages.success(request, f'Kayıt Başarılı !!')
        return redirect("/")
    else:
        context = {
            'site': site,
            'slide':slide,
            'ürün_list':ürün_list,
        }
        return render(request, "base.html",context)


def hesap_guncelleme(request): 
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        username = request.POST["username"]
        email    = request.POST["email"]
        parolam  = request.POST["parolam"]
        telefon  = request.POST["iletisim"]
        adres    = request.POST["adres"]
        name     = request.POST["usernameasli"]
        ids      = request.POST["idsa"]

        user     = User.objects.get(username=name)

        messages.success(request, f'Kayıt Başarılı !!')
        return redirect("/")
    else:
        return redirect("/")



def login_view(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if len(username) >= 40 or len(password) >= 60:
            messages.info(request, f'Hatalı Giriş Yaptınız !')
            return redirect('/')


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
