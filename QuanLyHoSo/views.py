from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import QuanLyHoSoForm
from .forms import QuanLyHDLDForm
from django.contrib.auth.decorators import login_required
from ThongTin.models import DonVi,DoiTuongCanBo
from datetime import datetime

@login_required
def DanhSachHoSo(request):
   alertContent = request.GET.get('alertContent')
   listHoSo = CanBo.objects.all().order_by('-id')
   dateNow = datetime.now().date()
   return render(request, 'danhSachHoSo.html', {'listHoSo': listHoSo,'dateNow': dateNow, 'alertContent': alertContent})

@login_required
def ThemHoSo(request):
    cacDonVi = DonVi.objects.all().order_by('-id')
    cacDoiTuongCanBo = DoiTuongCanBo.objects.all().order_by('-id')
    if request.method == 'POST':
        form = QuanLyHoSoForm(request.POST)
        data_copy = request.POST.copy()
        
        form.data = data_copy
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('danhSachHoSo') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = QuanLyHoSoForm()
    return render(request, 'themhoso.html', {'form': form, 'cacDonVi': cacDonVi,'cacDoiTuongCanBo': cacDoiTuongCanBo})

@login_required
def SuaHoSo(request, id):
    hoSo = get_object_or_404(CanBo, id=id)
    if request.method == 'POST':
        hoSo.maVCNLD = request.POST.get('maVCNLD')
        hoSo.maCanBo = request.POST.get('maCanBo')
        hoSo.hoTen = request.POST.get('hoTen')
        hoSo.ngaySinh = request.POST.get('ngaySinh')
        hoSo.gioiTinh = request.POST.get('gioiTinh')
        hoSo.soDienThoai = request.POST.get('soDienThoai')
        hoSo.email = request.POST.get('email')
        hoSo.queQuan = request.POST.get('queQuan')
        hoSo.thoiGianBatDauCT = request.POST.get('thoiGianBatDauCT')
        hoSo.trangThai = request.POST.get('trangThai')
        hoSo.isLanhDao = request.POST.get('isLanhDao')
        hoSo.isKiemNhiemNoiKhac = request.POST.get('isKiemNhiemNoiKhac')
        hoSo.isGiangVien = request.POST.get('isGiangVien')
        hoSo.isNghienCuuVien = request.POST.get('isNghienCuuVien')
        hoSo.donVi  = get_object_or_404(DonVi, id=request.POST.get('donVi'))
        hoSo.doiTuongCanBo  = get_object_or_404(DoiTuongCanBo, id=request.POST.get('doiTuongCanBo'))
        hoSo.hinhThucGiaoKet = request.POST.get('hinhThucGiaoKet')
        hoSo.save()
        alert_content = 'Sửa'
        url = reverse('danhSachHoSo') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        mucHocPhi = CanBo.objects.get(id=id)
        form = QuanLyHoSoForm()

    cacDonVi = DonVi.objects.all().order_by('-id')
    cacDoiTuongCanBo = DoiTuongCanBo.objects.all().order_by('-id')
    return render(request, 'suaHoSo.html', {'form': form, 'hoSo': hoSo, 'cacDonVi': cacDonVi,'cacDoiTuongCanBo': cacDoiTuongCanBo})

@login_required
def XoaHoSo(request, id):
    hoSo = get_object_or_404(CanBo, id=id)
    if request.method == 'POST':
        hoSo.delete()
        alert_content = 'Xóa'
        url = reverse('danhSachHoSo') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaHoSo.html', {'hoSo': hoSo})

@login_required
def DanhSachHDLD(request):
   alertContent = request.GET.get('alertContent')
   listHDLD = HopDongLaoDong.objects.all().order_by('-id')
   dateNow = datetime.now().date()
   return render(request, 'danhSachHDLD.html', {'listHDLD': listHDLD,'dateNow': dateNow, 'alertContent': alertContent})

@login_required
def ThemHDLD(request):
    cacNLD = VienChucNLD.objects.all().order_by('-id')
    cacHopDong = HopDong.objects.all().order_by('-id')
    if request.method == 'POST':
        form = QuanLyHDLDForm(request.POST)
        data_copy = request.POST.copy()
        
        form.data = data_copy
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('danhSachHDLD') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = QuanLyHDLDForm()
    return render(request, 'themHDLD.html', {'form': form, 'cacNLD': cacNLD,'cacHopDong': cacHopDong})

@login_required
def SuaHDLD(request, id):
    HDLD = get_object_or_404(CanBo, id=id)
    if request.method == 'POST':
        HDLD.maVCNLD =  get_object_or_404(VienChucNLD, id=request.POST.get('maVCNLD'))
        HDLD.tenHD = get_object_or_404(HopDong, id=request.POST.get('tenHD'))
        HDLD.soHD=request.POST.get('soHD')
        HDLD.diaDiem=request.POST.get('diaDiem')
        HDLD.ngayKy=request.POST.get('ngayKy')
        HDLD.ngayCoHieuLuc=request.POST.get('ngayCoHieuLuc')
        HDLD.ngayHetHan=request.POST.get('ngayHetHan')
        HDLD.ghiChu=request.POST.get('ghiChu')
        HDLD.save()
        alert_content = 'Sửa'
        url = reverse('danhSachHDLD') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        form = QuanLyHDLDForm()

    cacNLD = VienChucNLD.objects.all().order_by('-id')
    cacHopDong = HopDong.objects.all().order_by('-id')
    return render(request, 'suaHDLD.html', {'form': form, 'HDLD': HDLD, 'cacNLD': cacNLD,'cacHopDong': cacHopDong})

@login_required
def XoaHDLD(request, id):
    HDLD = get_object_or_404(HopDongLaoDong, id=id)
    if request.method == 'POST':
        HDLD.delete()
        alert_content = 'Xóa'
        url = reverse('danhSachHDLD') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaHDLD.html', {'HDLD': HDLD})