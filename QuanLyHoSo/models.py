from django.db import models
from ThongTin.models import DonVi, DoiTuongCanBo

class CanBo(models.Model):
    maVCNLD = models.CharField(max_length=10)
    maCanBo = models.CharField(max_length=10)
    hoTen = models.CharField(max_length=100)
    ngaySinh = models.DateField()
    donVi = models.ForeignKey(DonVi, on_delete = models.CASCADE)
    gioiTinh = models.BooleanField(blank=True)
    queQuan = models.CharField(max_length=100,blank=True, null=True)
    soDienThoai = models.CharField(max_length=12)
    email = models.EmailField(blank=True, null=True)
    thoiGianBatDauCT = models.DateField(blank=True, null=True)
    trangThai = models.BooleanField(blank=True)
    isLanhDao = models.BooleanField(blank=True)
    isKiemNhiemNoiKhac = models.BooleanField(blank=True)
    isGiangVien = models.BooleanField(blank=True)
    isNghienCuuVien = models.BooleanField(blank=True)
    doiTuongCanBo = models.ForeignKey(DoiTuongCanBo, on_delete = models.CASCADE)
    hinhThucGiaoKet = models.CharField(max_length=100,blank=True, null=True)
class VienChucNLD(models.Model):
    maVCNLD = models.CharField(max_length=10)
    hoTen = models.CharField(max_length=100)

class HopDong(models.Model):
    tenHD=models.CharField(max_length=100)
class HopDongLaoDong(models.Model):
    maVCNLD = models.ForeignKey(VienChucNLD,on_delete=models.CASCADE)
    tenHD=models.ForeignKey(HopDong,on_delete=models.CASCADE)
    soHD=models.CharField(max_length=10)
    diaDiem=models.CharField(max_length=100)
    ngayKy=models.DateField(blank=True, null=True)
    ngayCoHieuLuc=models.DateField(blank=True, null=True)
    ngayHetHan=models.DateField(blank=True, null=True)
    ghiChu=models.CharField(max_length=200)

