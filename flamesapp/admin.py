from django.contrib import admin
from . models import Flames


class FlamesAdmin(admin.ModelAdmin):
    list_display = ['name1', 'name2', 'result']


# Register your models here.
admin.site.register(Flames, FlamesAdmin)