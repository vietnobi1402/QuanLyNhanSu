from .models import *
from django import forms

class QuanLyHoSoForm(forms.ModelForm):
    class Meta:
        model = CanBo
        fields = ['maVCNLD', 'maCanBo', 'hoTen','ngaySinh','donVi','gioiTinh','queQuan','soDienThoai','thoiGianBatDauCT','trangThai','isLanhDao'
                  ,'isKiemNhiemNoiKhac','isGiangVien','isNghienCuuVien','doiTuongCanBo','hinhThucGiaoKet']

class QuanLyHDLDForm(forms.ModelForm):
    class Meta:
        model = HopDongLaoDong
        fields = ['maVCNLD', 'tenHD', 'soHD','diaDiem','ngayKy','ngayCoHieuLuc','ngayHetHan','ghiChu']