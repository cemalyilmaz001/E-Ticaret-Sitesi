from django.contrib import admin
from .models import Email_Abonelik, Yardım, kkb_hesabim, Site_Ayarları, Slide_Gösterisi, Ürün_Listesi, İletişim, Sepetim

# Register your models here.

admin.site.register(Email_Abonelik)
admin.site.register(Site_Ayarları)
admin.site.register(Slide_Gösterisi)
admin.site.register(Ürün_Listesi)
admin.site.register(İletişim)
admin.site.register(kkb_hesabim)
admin.site.register(Yardım)
admin.site.register(Sepetim)