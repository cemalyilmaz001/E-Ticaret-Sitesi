from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Site_Ayarları, Slide_Gösterisi, Email_Abonelik, Ürün_Listesi, İletişim, kkb_hesabim, Yardım, Sepetim

site        = Site_Ayarları.objects.all()
slide       = Slide_Gösterisi.objects.all()
ürün_list   = Ürün_Listesi.objects.all()
kkb_hesap   = kkb_hesabim.objects.all()
ssss        = Yardım.objects.all()

def sepet_adet(request):
    adet = 0
    for sepetim in Sepetim.objects.all():
        if sepetim.kullanici.username == request.user.username:
            adet += int(sepetim.total_atted)
    return adet

# Ana Sayfa
def index(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
        'adets':sepet_adet(request),
    }
    return render(request, "base.html",context)

# Biz Kimiz
def bzkmz(request):
    global site
    global slide
    global ürün_list
    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
        'adets':sepet_adet(request),
    }
    return render(request, "bzkm.html",context)

# Yardım
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
        'adets':sepet_adet(request),
    }
    return render(request, "sorular.html", context)

# Email Gönder
def email_abonelik(request):
    if request.method == 'POST':
        abone = request.POST["email_abonelik"]
        email = Email_Abonelik.objects.create(email_address=abone)
        email.save()
        messages.success(request, f'Kayıt Başarılı !!')
        return redirect("/")
    else:
        return redirect("/")

# İletişim
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
            'adets':sepet_adet(request),
        }
        return render(request, "iletişim.html",context)

# Sepetim
def mybasket(request):
    global site
    global slide
    global ürün_list

    toplam_fiyat = 0
    for i in Sepetim.objects.all():
        if i.kullanici.username == request.user.username:
            toplam_fiyat  += int(i.ürün_fiyat) * int(i.total_atted)

    #for r in SepetOnay.objects.all():
    #    if r.sepet.kullanici.username == request.user.username:
    #        r.sepet_total_fiyati = int(toplam_fiyat)
    #        r.save()
    #    else:
    #        for i in Sepetim.objects.all():
    #            if i.kullanici.username == request.user.username:
    #                SepetOnay.objects.create(sepet=i,sepet_total_fiyati=int(toplam_fiyat)).save()

    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
        'sepetim':Sepetim.objects.all(),
        'fiyat':toplam_fiyat,
        'adets':sepet_adet(request),
    }
    return render(request, "basket.html",context)

# Sepete Ekle 
@login_required
def create_sepet(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        ürün_name   = request.POST["ürün_name"]
        ürün_fiyat  = request.POST["ürün_fiyat"]
        totalfiyat = 0
        e = 0
        for i in Sepetim.objects.all():
            if i.kullanici.username == request.user.username:
                if i.ürün.ürün_price == ürün_fiyat:
                    e += 1
                    for w in Ürün_Listesi.objects.filter(ürün_price=ürün_fiyat):
                        if w.ürün_price == ürün_fiyat:
                            i.total_atted += 1
                            i.save()
        if e == 0:
            for w in Ürün_Listesi.objects.filter(ürün_price=ürün_fiyat):
                if w.ürün_price == ürün_fiyat:
                    a = Sepetim.objects.create(kullanici=request.user,ürün=w, ürün_fiyat=int(ürün_fiyat), total_atted=1).save()

        messages.success(request, f'Sepete Eklendi !!')
        return redirect("/")
    else:
        return redirect("/")

# Sepet deki ürün silme 
@login_required
def sepet_delete(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        ids     = request.POST["ids"]
        Sepetim.objects.filter(id=int(ids)).delete()
        messages.success(request, f'Ürün Kaldırıldı !!')
        return redirect("/mybasket")
    else:
        return redirect("/")

@login_required
def sepet_eksi(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        eksi     = request.POST["eksideger"]
        sepet = Sepetim.objects.filter(id=int(eksi))
        for i in sepet:
            if i.total_atted == 1:
                Sepetim.objects.filter(id=int(eksi)).delete()
            else:
                i.total_atted -= 1

            i.save()

        messages.success(request, f'Ürün Düşürüldü !!')
        return redirect("/mybasket")
    else:
        return redirect("/")

@login_required
def sepet_arti(request):
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        arti     = request.POST["artideger"]
        sepet = Sepetim.objects.filter(id=int(arti))
        for i in sepet:
            i.total_atted += 1
            i.save()
        messages.success(request, f'Ürün Artırıldı !!')
        return redirect("/mybasket")
    else:
        return redirect("/")

# Profil
@login_required
def myprofil(request):
    global site
    global slide
    global ürün_list
    global kkb_hesap

    context = {
        'site': site,
        'slide':slide,
        'ürün_list':ürün_list,
        'hesap':kkb_hesap,
        'adets':sepet_adet(request),
    }
    return render(request, "myprofil.html", context)

@login_required
def imageUpdate(request):  
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        image = request.FILES["image_update"]
        name  = request.POST["name"]
        # request.user.id
        new_hesap = kkb_hesabim.objects.get(adi_soyadi=f"{str(name)}")
        new_hesap.profil_photo = image
        new_hesap.save()

        messages.success(request, f'Profil Resmi Güncellendi !!')
        return redirect("/")
    else:
        return redirect("/")

@login_required
def hesap_guncelleme(request): 
    global site
    global slide
    global ürün_list

    if request.method == "POST":
        usernames = request.POST["username"]
        name      = request.POST["usernameasli"]
        emails    = request.POST["email"]
        parolam   = request.POST["parolam"]
        telefon   = request.POST["iletisim"]
        adres     = request.POST["adres"]
        t = 0
        for r in User.objects.all():
            if r.username == usernames:
                t += 1

        user      = User.objects.get(id=request.user.id)
        new_hesap = kkb_hesabim.objects.get(adi_soyadi=f"{str(name)}")

        user.email    = emails

        if t == 0:
            user.username           = usernames
            new_hesap.adi_soyadi    = usernames

        new_hesap.email          = emails
        new_hesap.iletişim_tel   = telefon
        new_hesap.kargo_adres    = adres
        new_hesap.save()

        if parolam != "parolam":
            user.set_password(f'{str(parolam)}')

        user.save()

        messages.success(request, f'Hesabınız Güncellendi !!')
        return redirect("/myprofil")
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
            return redirect('/login')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f' Hoşgeldiniz {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'Hatalı Giriş Yaptınız !')
            return redirect('/login')
    else:
        context = {
            'site': site,
            'slide':slide,
            'ürün_list':ürün_list,
            'adets':sepet_adet(request),
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
            new_hesap = kkb_hesabim.objects.create(adi_soyadi=f"{str(username)}", profil_photo="", email=f"{str(email)}", iletişim_tel="", kargo_adres="", kkkart_numarasi="", kkkart_ay="",kkkart_yil="",kkkart_cvv="")
            new_hesap.save()
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
            'adets':sepet_adet(request),
        }
        return render(request, "register.html",context)

def logout_view(request):
    logout(request)
    return redirect('/')
