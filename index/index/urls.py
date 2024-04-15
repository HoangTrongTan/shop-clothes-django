"""
URL configuration for index project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from USER import views as user
from ADMIN import views as adm 
#upload file
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',user.home,name="home"),
    path('detail/<int:id>/',user.detail),
    path('adm/',adm.index,name="adm"),
    path('adm__add/',adm.Add,name="add_sp"),
    path('adm_sua/',adm.Sua,name="sua_sp"),
    path('adm_xoa/<int:id>',adm.Xoa,name="xoa_sp"),
    path('login_admin/',adm.Login,name="log_ad"),
    path('regisadm/',adm.register,name="regis_adm"),
    path('ThemMaLoai/',adm.ThemMaLoai,name="ThemMaLoai"),
    path('SuaMaLoai/',adm.SuaMaLoai,name="SuaMaLoai"),
    path('XoaMaloaiSp/<int:id>',adm.XoaMaloaiSp,name="XoaMaloaiSp"),
    path('SuaMaGiamGia/',adm.SuaMaGiamGia,name="SuaMagiamgia"),
    path('XoaGiamGia/<int:id>',adm.XoaGiamGia,name="XoaGiamGia"),


    # USER
    path('ShopList/',user.ShopList,name="ShopList"),
    path('TimKemTheoLoai/<int:id>',user.TimKemTheoLoai,name="TimKemTheoLoai"),
    path('Contact/',user.Contact,name="Contact"),
    path('FindByPrice/<str:gia>',user.FindByPrice,name="FindByPrice"),

    #Cart
    path('Cart/',user.Cart,name="Cart"),
    path('CartForm/',user.CartForm,name="CartForm"),
    path('AddCart/<int:id>',user.AddCart,name="AddCart"),
    path('DelCard/<int:id>',user.DelCard,name="DelCard"),

    #Bill
    path('Bill/',user.Bill,name="Bill"),


    #Login
    path('Login_user/',user.Login,name="Login_user"),
    path('Register/',user.Register,name="Register"),

    #Thông tin đặt hàng
    path('viewDatHang/',user.viewDatHang,name="viewDatHang"),
    path('AddThongtinDatHang/',user.AddThongtinDatHang,name="AddThongtinDatHang"),
    path('deleteDsDatHang/<int:id>',user.deleteDsDatHang,name="deleteDsDatHang"),


    path('clear_sessionUser/',user.clear_sessionUser,name="clear_sessionUser"),
    path('deleteDsDatHang/<int:id>',user.deleteDsDatHang,name="deleteDsDatHang"),
    path('search/',user.search,name="search"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
