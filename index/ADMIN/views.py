from django.shortcuts import render,redirect
from django.core.serializers.json import DjangoJSONEncoder
from USER.models import Ao,LoaiAo
from ADMIN.models import Admin_account as adm_ac
from django.contrib import messages
import json
import os
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    if 'email' in request.session:
        page_number = request.GET.get('page')

        listmaloai = LoaiAo.objects.all()
        paginator_maloai = Paginator(listmaloai,2)
        page_obj_maloai = paginator_maloai.get_page(page_number)

        listobj = Ao.objects.all().order_by("id_ao")
        paginator = Paginator(listobj,2)
        page_obj = paginator.get_page(page_number)

        list_json = json.dumps(
            [{'id_ao': obj.id_ao, 'ten_ao': obj.ten_ao, 'soluong': float(obj.soluong), 'giatien': str(obj.giatien), 'anh':str(obj.anh) , 'mo_ta': obj.mo_ta,'sale_price': obj.sale_price} for obj in listobj],
            cls=DjangoJSONEncoder
        )
        list_json_maloai = json.dumps(
            [{'id_loaiao': obj.id_loaiao, 'type_name': obj.type_name} for obj in listmaloai],
            cls=DjangoJSONEncoder
        )

        context = {
            'listobj':page_obj,
            'list_json':list_json,
            'listmaloai':page_obj_maloai,
            'list_json_maloai':list_json_maloai,
        }
        return render(request,'Admin_index.html',context)
    else:
        return redirect('log_ad')
def Add(request):
    if request.method == "POST":
        try:
            obj = Ao()
            obj.ten_ao = request.POST.get("tenao")
            obj.soluong = request.POST.get("soluong")
            obj.giatien = request.POST.get("giatien")
            obj.mo_ta = request.POST.get("mota")
            obj.sale_price = request.POST.get("Sale")
            obj.type_prodc = request.POST.get("type_prodct")
            if len(request.FILES) != 0:
                obj.anh = request.FILES['anh']
            obj.save()
            messages.success(request,"ok thêm thành công")
            return redirect("/adm")
        except Exception as e:
            print("lỗi\n\n\n",str(e))
    else:
        print("\n\n\nkhông có\n\n\n")
    return redirect("/adm")
def Sua(request):
    if request.method == "POST":
        obj = Ao()
        obj.id_ao = request.POST.get("index_ao")
        obj.ten_ao = request.POST.get("tenao")
        obj.soluong = request.POST.get("soluong")
        obj.giatien = request.POST.get("giatien")
        obj.mo_ta = request.POST.get("mota")
        obj.sale_price = request.POST.get("Sale")

        obj_old = Ao.objects.get(id_ao=obj.id_ao)
        if obj_old.anh != "":
            if len(obj_old.anh) > 0:
                os.remove(obj_old.anh.path)
        if len(request.FILES) != 0:
            obj.anh = request.FILES['anh']
        obj.save()
        messages.success(request,"ok thêm thành công")
        return redirect('/adm')
    return redirect('/adm')
def Xoa(request,id):
    obj = Ao.objects.get(id_ao=id)
    if obj.anh != "":
            if len(obj.anh) > 0:
                os.remove(obj.anh.path)
    obj.delete()
    messages.success(request,"ok xóa thành công")
    return redirect('/adm')

def Login(request):
    if request.POST.get("dangnhap"):
        email = request.POST.get("email_acc")
        passwd = request.POST.get("pass_ac")
        try:
            list_obj = adm_ac.objects.get(email=email,passwd = passwd)
            request.session['email'] = list_obj.email
            return redirect('adm')
        except:
            return redirect('log_ad')
    return render(request,"login.html")

def register(request):
    if request.POST.get("dangky"):
        obj = adm_ac()
        obj.email = request.POST.get("eamil_acc")
        obj.passwd = request.POST.get("pass_ac")
        try:
            obj.save()
            messages.success(request,"đăng kí thành công")
            return redirect('log_ad')
        except: 
            return render(request,'forgot-password.html')
    messages.success(request,"đăng kí thành công")
    return render(request,"register.html")

def ThemMaLoai(request):
    if request.method == "POST":
        obj = LoaiAo()
        obj.type_name = request.POST.get("TenLoai")
        obj.save()
        return redirect('adm')
    return redirect('adm')
def SuaMaLoai(request):
    if request.method == "POST":
        id_loaiao = request.POST.get("idmaloai")
        obj = LoaiAo.objects.get(id_loaiao=id_loaiao)
        obj.type_name = request.POST.get("TenLoai")
        obj.save()
        return redirect('adm')
    return redirect('adm')
def XoaMaloaiSp(request,id):
    obj = LoaiAo.objects.get(id_loaiao=id)
    obj.delete()
    return redirect('adm')

def SuaMaGiamGia(request):
    if request.method == "POST":
        id = request.POST.get("id_loaiao")
        magiamgia = request.POST.get("sale")
        obj = Ao.objects.get(id_ao=id)
        obj.sale_price = magiamgia
        obj.save()
        return redirect('adm')
def XoaGiamGia(request,id):
    obj = Ao.objects.get(id_ao=id)
    obj.sale_price = 0
    obj.save()
    return redirect('adm')
#register.html