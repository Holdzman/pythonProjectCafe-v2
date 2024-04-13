from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_cafe.models import Drink, Hotdog, Spicy, Hotdog_Spicy


# Register your models here.
class HotdogSpiceInline(admin.TabularInline):
    model = Hotdog_Spicy


@admin.register(Hotdog)
class HotdogAdmin(ModelAdmin):
    list_display = ('name', 'price', 'cover')
    inlines = [HotdogSpiceInline]
    readonly_fields = ('data_create', 'data_update')


admin.site.register(Drink)
admin.site.register(Spicy)
admin.site.register(Hotdog_Spicy)
