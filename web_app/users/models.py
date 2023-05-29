from django.db import models

# Create your models here.

class Site_Ayarları(models.Model):
    site_title   = models.CharField(max_length=50)
    navbar_title = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    keywords     = models.CharField(max_length=50)
    bizkmz_text  = models.CharField(max_length=550)
    yardım_tel   = models.CharField(max_length=12)

class Yardım(models.Model):
    yrdm_title       = models.CharField(max_length=50)
    yrdm_description = models.CharField(max_length=250)
    yrdm_keywords    = models.CharField(max_length=150)

# Kayıtlı Email Adreslerine Bilgi gönderilecek.
class Email_Abonelik(models.Model):
    email_address = models.CharField(max_length=50)

# Değişen görseller Slide.
class İletişim(models.Model):
    email = models.CharField(max_length=50)
    ad    = models.CharField(max_length=50)
    istek = models.TextField()

# Değişen görseller Slide.
class Slide_Gösterisi(models.Model):
    slide_image  = models.ImageField(upload_to='image/') 
    slide_title  = models.CharField(max_length=150)
    slide_descrp = models.CharField(max_length=150)

# Kullanıcı Bilgileri
class kkb_hesabim(models.Model):
    adi_soyadi      = models.CharField(max_length=50)
    profil_photo    = models.ImageField(upload_to='image/') 
    email           = models.CharField(max_length=50)
    iletişim_tel    = models.CharField(max_length=50)
    kargo_adres     = models.CharField(max_length=50)
    kkkart_numarasi = models.CharField(max_length=30)
    kkkart_ay       = models.CharField(max_length=30)
    kkkart_yil      = models.CharField(max_length=30)
    kkkart_cvv      = models.CharField(max_length=30)

# Ürünler
class Ürün_Listesi(models.Model):
    ürün_image_name = models.ImageField(upload_to='image/') 
    ürün_descrption = models.CharField(max_length=50)
    ürün_price      = models.CharField(max_length=50)

class Sepetim(models.Model):
    kullanici = models.ForeignKey(
        "kkb_hesabim",
        on_delete=models.CASCADE,
    )

    ürün = models.ForeignKey(
        "Ürün_Listesi",
        on_delete=models.CASCADE,
    )
    ürün_fiyat      = models.IntegerField()
    total_fiyat     = models.IntegerField()