# Generated by Django 4.2.9 on 2024-02-22 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyHoSo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HopDong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenHD', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VienChucNLD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maVCNLD', models.CharField(max_length=10)),
                ('hoTen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HopDongLaoDong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soHD', models.CharField(max_length=10)),
                ('diaDiem', models.CharField(max_length=100)),
                ('ngayKy', models.DateField(blank=True, null=True)),
                ('ngayCoHieuLuc', models.DateField(blank=True, null=True)),
                ('ngayHetHan', models.DateField(blank=True, null=True)),
                ('ghiChu', models.CharField(max_length=200)),
                ('maVCNLD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyHoSo.vienchucnld')),
                ('tenHD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyHoSo.hopdong')),
            ],
        ),
    ]
