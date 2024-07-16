from django.contrib import admin
from .models import SiteConfiguration, Modal, Footer, Home

# Register your models here.
class SiteConfigurationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ModalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class FooterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(Modal, ModalAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Home, HomeAdmin)
