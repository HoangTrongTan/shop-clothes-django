from django.db import models
from django.db.models.signals import pre_delete,pre_save
from django.dispatch import receiver
import os
from django.conf import settings

class LoaiAo(models.Model):
    id_loaiao = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100,null=False)

# Create your models here.
class Ao(models.Model):
    id_ao      = models.AutoField(primary_key=True)
    ten_ao     = models.CharField(max_length=100,null=False)
    soluong    = models.IntegerField()
    giatien    = models.DecimalField(max_digits=30,decimal_places=3)
    mo_ta      = models.TextField()
    anh        = models.ImageField(upload_to='images',null=False,default=None)
    type_prodc = models.IntegerField(LoaiAo,default=0)
    sale_price = models.DecimalField(max_digits=30,decimal_places=3)


#====================================================Card=========================================================
class Ao_temp(models.Model):
    id_ao    = models.IntegerField(primary_key=True)
    ten_ao   = models.CharField(max_length=100,null=False)
    soluong  = models.IntegerField()
    giatien  = models.DecimalField(max_digits=30,decimal_places=3)
    tongtien = models.IntegerField(default=0)
    anh      = models.CharField(max_length=200,null=False)
    taikhoan = models.CharField(max_length=100,null=False,default="")

#====================================================Card=========================================================
class Ao_favourite(models.Model):
    id_ao    = models.IntegerField(primary_key=True)
    ten_ao   = models.CharField(max_length=200,null=False)
    giatien  = models.IntegerField()
    anh      = models.CharField(max_length=200,null=False)
    taikhoan = models.CharField(max_length=200,null=False)

#====================================================Login=========================================================
class Account(models.Model):
    id_taikhoan = models.AutoField(primary_key=True)
    acc_name    = models.CharField(max_length=100,null=False,default="",unique=True)
    pass_user   = models.CharField(max_length=100,null=False,unique=True)
    owner_name  = models.CharField(max_length=100,null=False,unique=True)
    email_user  = models.CharField(max_length=200,null=False,unique=True)
    owner_img   = models.ImageField(upload_to='images',null=False,default=None)

#====================================================ThongTinDatHang==================================================
class ThongTinDatHang(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=200,default="")
    thongtinsanpham = models.CharField(max_length=200)
    tongtien = models.IntegerField()
    dienthoai = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    diachi = models.CharField(max_length=200)
    taikhoan = models.CharField(max_length=100,default="")



