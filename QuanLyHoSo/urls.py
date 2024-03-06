from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.DanhSachHoSo)),
   path('danhsachhoso', login_required(views.DanhSachHoSo), name="danhSachHoSo"),
   path('danhsachhoso/', login_required(views.DanhSachHoSo), name="danhSachHoSo"),
   path('themhoso/', login_required(views.ThemHoSo), name='themHoSo'),
   path('<int:id>/update/', login_required(views.SuaHoSo), name='suaHoSo'),
   path('<int:id>/delete/', login_required(views.XoaHoSo), name='xoaHoSo'),

   path('danhsachHDLD', login_required(views.DanhSachHDLD), name="danhSachHDLD"),
   path('danhsachHDLD/', login_required(views.DanhSachHDLD), name="danhSachHDLD"),
   path('themHDLD/', login_required(views.ThemHDLD), name='themHDLD'),
   path('<int:id>/update/', login_required(views.SuaHDLD), name='suaHDLD'),
   path('<int:id>/delete/', login_required(views.XoaHDLD), name='xoaHDLD'),
]