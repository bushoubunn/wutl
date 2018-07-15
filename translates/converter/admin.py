from django.contrib import admin
from .models import Kansaikotoba,Futugo

# Register your models here.
class KansaikotobaAdmin(admin.ModelAdmin):
    list_display=('kotoba','kanji','is_has_kanji','id')

admin.site.register(Kansaikotoba,KansaikotobaAdmin)
class FutugoAdmin(admin.ModelAdmin):
    list_display=('yakubun','ori_kotoba','example')
admin.site.register(Futugo,FutugoAdmin)