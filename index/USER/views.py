from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
from .models import Ao,LoaiAo,Account,Ao_temp,ThongTinDatHang
# Create your views here.
def home(request):
    if 'taikhoan' in request.session:
        ao_list = Ao.objects.all().order_by('-giatien')
        LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
        img_user = Account.objects.get(email_user=request.session['email_user'])

        list_loai_quanlity = []
        for loai_ao in LoaiAo_list:
            count = ao_list.filter(type_prodc=loai_ao.id_loaiao).count()
            list_temp = [loai_ao.id_loaiao, loai_ao.type_name, count]
            list_loai_quanlity.append(list_temp)
        for i in range(len(ao_list)):
                if ao_list[i].sale_price > 0:
                    ao_list[i].sale_price = ao_list[i].giatien - (ao_list[i].giatien * ao_list[i].sale_price / 100) 
        list_aotemp = Ao_temp.objects.filter(taikhoan=request.session['taikhoan']).values('id_ao')
        context = {
            'list':ao_list,
            'LoaiAo_list':LoaiAo_list,
            'list_loai_quanlity':list_loai_quanlity,
            'ANH':img_user.owner_img,
            'list_aotemp':list_aotemp,
        }
        

        request.session['soluonggiohang'] = Ao_temp.objects.filter(taikhoan=request.session['taikhoan']).count()
        return render(request,'index.html', context)
    return redirect('Login_user')

#tìm kiếm theo loại
def TimKemTheoLoai(request,id):
    ao_list = Ao.objects.filter(type_prodc=id).order_by('-giatien')
    ao_list2 = Ao.objects.all().order_by('-giatien')
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    list_loai_quanlity = []
    for loai_ao in LoaiAo_list:
        count = ao_list2.filter(type_prodc=loai_ao.id_loaiao).count()
        list_temp = [loai_ao.id_loaiao, loai_ao.type_name, count]
        list_loai_quanlity.append(list_temp)
    for i in ao_list:
            if i.sale_price > 0:
                i.sale_price = i.giatien - (i.giatien * i.sale_price / 100) 
    list_aotemp = Ao_temp.objects.filter(taikhoan=request.session['taikhoan']).values('id_ao')
    context = {
         'list':ao_list,
         'LoaiAo_list':LoaiAo_list,
         'list_loai_quanlity':list_loai_quanlity,
         'list_aotemp':list_aotemp,
    }
    return render(request,'index.html', context)
def detail(request,id):
    obj = Ao.objects.get(id_ao=id)
    obj_related = Ao.objects.filter(type_prodc=obj.type_prodc)
    context = {
        'obj': obj,
        'obj_related': obj_related,
    }
    
    return render(request,"detail.html",context)
#===================================================Shop============================================================================
def getlist():
    return 
def ShopList(request):
    ao_list = Ao.objects.all().order_by('-giatien')
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    list_filterBy_price = [
         {'gia':'0 đ - 300.000 đ', 'soluong':Ao.objects.filter(giatien__gte=0,giatien__lte=300).count(), 'STT':1,'so1':0,'so2':300},
         {'gia':'100.000 đ - 300.000 đ','soluong':Ao.objects.filter(giatien__gte=100,giatien__lte=300).count() , 'STT':2,'so1':100,'so2':300},
         {'gia':'300.000 đ - 500.000 đ','soluong':Ao.objects.filter(giatien__gte=300,giatien__lte=500).count() , 'STT':3, 'so1':300, 'so2':500},
         {'gia':'500.000 đ - 700.000 đ','soluong':Ao.objects.filter(giatien__gte=500,giatien__lte=700).count() , 'STT':4, 'so1':500, 'so2':700},
         {'gia':' > 700.000 đ','soluong':Ao.objects.filter(giatien__gte=700).count() , 'STT':5, 'so1':700,'so2':700},
    ]
    context = {
         'list':ao_list,
         'LoaiAo_list':LoaiAo_list,
         'list_filterBy_price':list_filterBy_price,
    }
    return render(request,'shop.html', context)
def FindByPrice(request,gia):
    tachgia = gia.split("-")
    ao_list = None
    if(int(tachgia[0]) == int(tachgia[0])):
        ao_list = Ao.objects.filter(giatien__gte=tachgia[0],giatien__lte=tachgia[1])
    ao_list = Ao.objects.filter(giatien__gte=tachgia[0],giatien__lte=tachgia[1])
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    list_filterBy_price = [
         {'gia':'0 đ - 300.000 đ', 'soluong':Ao.objects.filter(giatien__gte=0,giatien__lte=300).count(), 'STT':1,'so1':0,'so2':300},
         {'gia':'100.000 đ - 300.000 đ','soluong':Ao.objects.filter(giatien__gte=100,giatien__lte=300).count() , 'STT':2,'so1':100,'so2':300},
         {'gia':'300.000 đ - 500.000 đ','soluong':Ao.objects.filter(giatien__gte=300,giatien__lte=500).count() , 'STT':3, 'so1':300, 'so2':500},
         {'gia':'500.000 đ - 700.000 đ','soluong':Ao.objects.filter(giatien__gte=500,giatien__lte=700).count() , 'STT':4, 'so1':500, 'so2':700},
         {'gia':' > 700.000 đ','soluong':Ao.objects.filter(giatien__gte=700).count() , 'STT':5, 'so1':700,'so2':700},
    ]
    context = {
         'list':ao_list,
         'LoaiAo_list':LoaiAo_list,
         'list_filterBy_price':list_filterBy_price,
    }
    return render(request,'shop.html', context)
    return redirect('ShopList')
#=======================================================Contact=========================================================================
def Contact(request):
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    context = {
         'LoaiAo_list':LoaiAo_list,
    }
    return render(request,"contact.html",context)
#=======================================================Card=========================================================================
def Cart(request):
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    list_aotemp = Ao_temp.objects.filter(taikhoan=request.session['taikhoan'])
    tongtien = 0
    for i in list_aotemp:
        tongtien += i.tongtien
    context = {
         'LoaiAo_list':LoaiAo_list,
         'list_aotemp':list_aotemp,
         'tongtien':tongtien - 10,
         'ship':10,
         'tien':tongtien
    }
    return render(request,'cart.html',context)
def AddCart(request,id):
    if request.session['taikhoan']:
        obj = Ao.objects.get(id_ao=id)
        if obj.soluong == 0:
            messages.warning(request,f"sản phẩm {obj.ten_ao} hiện đang hết hàng, chúng tôi sẽ cập nhật thêm (cô nai ni mát s ta aa !)")
            return redirect('Cart')
        obj_temp = Ao_temp()
        obj_temp.id_ao = obj.id_ao
        obj_temp.ten_ao = obj.ten_ao
        obj_temp.soluong = 1
        obj_temp.giatien = obj.giatien
        obj_temp.tongtien = obj.giatien
        obj_temp.anh = str(obj.anh)
        obj_temp.taikhoan = request.session['owner_name']
        obj_temp.save()
        obj.soluong -= 1
        obj.save()
        request.session[str(id)] = True
        messages.success(request,f"sản phẩm  {obj.ten_ao}  đã được thêm vào giỏ !!")
        request.session['soluonggiohang'] = Ao_temp.objects.all().count()
    return redirect('home')
def CartForm(request):
    if request.method == 'POST':
        sl = int( request.POST.get('Soluong') )
        id_ao = request.POST.get('id_ao')
        obj = Ao.objects.get(id_ao=id_ao)
        # trường hợp sản phẩm đã tồn tại trong giỏ hàng
        try:
            obj_temp = Ao_temp.objects.get(id_ao=id_ao)
            if obj_temp:
                if obj.soluong == 0:
                    messages.warning(request,f"sản phẩm {obj_temp.ten_ao} hiện đang hết hàng, chúng tôi sẽ cập nhật thêm (cô nai ni mát s ta aa !)")
                    return redirect('home')
                obj_temp.soluong = sl
                obj_temp.tongtien *= sl
                obj.soluong -= sl
                obj.save()
                obj_temp.save()
                messages.success(request,f"sản phẩm {obj_temp.ten_ao} đã được thêm vào giỏ !!")
                request.session['soluonggiohang'] = Ao_temp.objects.all().count()
                return redirect('home')    
        # trường hợp chưa tồn tại
        except:
            if sl > obj.soluong:
                messages.warning(request,f'số lượng không đủ sản phẩm chỉ còn {obj.soluong} cái !!')
            elif obj.soluong == 0:
                messages.warning(request,f'sản phẩm {obj.ten_ao} hiện đang hết hàng !!, chúng tôi sẽ cập nhật thêm (kà woa ị !)')
            else:
                obj_temp = Ao_temp()
                obj_temp.id_ao = id_ao
                obj_temp.ten_ao = obj.ten_ao
                obj_temp.soluong = sl
                obj_temp.giatien = obj.giatien
                obj_temp.tongtien = sl * int(obj.giatien)
                obj_temp.anh = str(obj.anh)
                obj_temp.taikhoan = request.session['taikhoan']
                obj_temp.save()
                obj.soluong -= sl
                obj.save()
                messages.success(request,f"Bạn đã thêm sản phẩm {obj.ten_ao} số lượng {sl} vào giỏ hàng !!")
                request.session['soluonggiohang'] = Ao_temp.objects.all().count()
            return redirect('home')
    return redirect('home')
def DelCard(request,id):
    objAo = Ao.objects.get(id_ao=id)
    obj = Ao_temp.objects.get(id_ao=id)
    objAo.soluong += obj.soluong
    objAo.save()
    obj.delete()
    messages.success(request,f"đã xóa {obj.ten_ao} khỏi giỏ hàng !")
    return redirect('Cart')
#=======================================================Card=========================================================================
def Bill(request):
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    obj_Acc = Account.objects.get(acc_name=request.session['taikhoan'])
    list_aotemp = Ao_temp.objects.filter(taikhoan=request.session['taikhoan'])
    tongtien = 0
    for i in list_aotemp:
        tongtien += i.tongtien
    context = {
         'LoaiAo_list':LoaiAo_list,
         'obj_Acc':obj_Acc,
         'list_aotemp':list_aotemp,
         'tongtien':tongtien - 10,
         'ship':10,
         'tien':tongtien
    }
    return render(request,'Bill.html',context)



#=======================================================Login=========================================================================
def Login(request):
    if request.method == "POST":
        try:
            obj = Account.objects.get(acc_name=request.POST.get("Taikhoan"),pass_user=request.POST.get("matkhau"))
            if obj:
                request.session['owner_name'] = obj.owner_name
                request.session['email_user'] = obj.email_user
                request.session['taikhoan'] = obj.acc_name
                messages.success(request,f"chào mừng {obj.owner_name} đăng nhập !!")
                return redirect("home")
        except:
            print("\n\n\nkhông phải\n\n\n")
            return redirect("Login_user")
    return render(request,'login_user.html')
def Register(request):
    if request.method == "POST":
        print("\n\n\nVòa\n\n\n")
        obj = Account()
        obj.acc_name = request.POST.get("taikhoan")
        obj.pass_user = request.POST.get("Matkhau")
        obj.owner_name = request.POST.get("Ten")
        obj.email_user = request.POST.get("Email")
        print(obj)
        if len(request.FILES) != 0:
             obj.owner_img = request.FILES['anh']
        obj.save()
        return redirect('Login_user')
    
#=======================================================ThongtindatHang=========================================================================
def AddThongtinDatHang(request):
    if request.method == 'POST':
        obj = Ao_temp.objects.all()
        obj_dathang = ThongTinDatHang()
        for i in obj:
            obj_dathang.thongtinsanpham += i.ten_ao+","+str(i.soluong)+","
        obj_dathang.ten = request.POST.get("ten")
        obj_dathang.dienthoai = request.POST.get("dienthoai")
        obj_dathang.email = request.POST.get("Email")
        obj_dathang.tongtien = request.POST.get("tongtien")
        obj_dathang.diachi = request.POST.get("diachi")
        obj_dathang.save()
        messages.success(request,"đặt hàng thành công !!")
        return redirect("home")
def viewDatHang(request):
    ls = ThongTinDatHang.objects.all()
    context = {
        "ls":ls,
    }
    return render(request,"danhsachdathang.html",context)
def is_number(char):
    return char.isdigit()
def deleteDsDatHang(request,id):
    obj = ThongTinDatHang.objects.get(id=id)
    obj.delete()
    messages.success(request,"Xóa thành công !!")
    return redirect("viewDatHang")
def clear_sessionUser(request):
    if 'taikhoan' in request.session:
        del request.session['taikhoan']
        return redirect("Login_user")
    else:
        messages.error(request,"Xóa thành công !!")
        return redirect("Login_user")
    
def search(request):
    text = request.GET.get("search")
    ao_list = Ao.objects.filter(Q(ten_ao__icontains=text))
    LoaiAo_list = LoaiAo.objects.all().order_by('id_loaiao')
    img_user = Account.objects.get(email_user=request.session['email_user'])

    list_loai_quanlity = []
    for loai_ao in LoaiAo_list:
        count = ao_list.filter(type_prodc=loai_ao.id_loaiao).count()
        list_temp = [loai_ao.id_loaiao, loai_ao.type_name, count]
        list_loai_quanlity.append(list_temp)
    for i in range(len(ao_list)):
            if ao_list[i].sale_price > 0:
                ao_list[i].sale_price = ao_list[i].giatien - (ao_list[i].giatien * ao_list[i].sale_price / 100) 
    list_aotemp = Ao_temp.objects.filter(taikhoan=request.session['taikhoan']).values('id_ao')
    context = {
        'list':ao_list,
        'LoaiAo_list':LoaiAo_list,
        'list_loai_quanlity':list_loai_quanlity,
        'ANH':img_user.owner_img,
        'list_aotemp':list_aotemp,
    }
    request.session['soluonggiohang'] = Ao_temp.objects.filter(taikhoan=request.session['taikhoan']).count()
    return render(request,'index.html', context)