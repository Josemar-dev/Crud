from django.contrib import admin
from .models import *

class menbroadmin(admin.ModelAdmin):
    list_display = "primeironome","segundonome","terceironome"

admin.site.register(menbro,menbroadmin)