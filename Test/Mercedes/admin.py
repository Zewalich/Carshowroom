from django.contrib import admin

from .models import carshowroom, Provider


# Register your models here.
@admin.register(carshowroom)
class carshowroomAdmin(admin.ModelAdmin):
    list_display = ['brand', 'provider', 'price']
    search_fields = ['brand__istartswith']
    list_per_page = 3

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email']