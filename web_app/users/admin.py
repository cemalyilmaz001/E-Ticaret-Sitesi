from django.contrib import admin
from .models import Email_Abonelik, Site_Ayarları, Slide_Gösterisi, Ürün_Listesi

# Register your models here.

admin.site.register(Email_Abonelik)
admin.site.register(Site_Ayarları)
admin.site.register(Slide_Gösterisi)
admin.site.register(Ürün_Listesi)

