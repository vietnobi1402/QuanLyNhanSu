# Generated by Django 4.2.9 on 2024-01-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoiTuongCanBo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loaiDoiTuong', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DonVi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenDonVi', models.CharField(max_length=100)),
            ],
        ),
    ]
