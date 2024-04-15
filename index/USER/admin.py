from django.contrib import admin
from USER.models import Ao
import os
# Register your models here.
class Employess(admin.ModelAdmin):
    list_display = ("id_ao","ten_ao","soluong","giatien","mo_ta","anh")
admin.site.register(Ao,Employess)