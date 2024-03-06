from django.db import models

class DonVi(models.Model):
    tenDonVi = models.CharField(max_length=100)

class DoiTuongCanBo(models.Model):
    loaiDoiTuong = models.CharField(max_length=100)

