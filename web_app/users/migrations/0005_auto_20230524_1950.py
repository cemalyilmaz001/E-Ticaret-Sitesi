# Generated by Django 3.2.18 on 2023-05-24 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_i̇letişim'),
    ]

    operations = [
        migrations.CreateModel(
            name='kkb_hesabim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi_soyadi', models.CharField(max_length=50)),
                ('profil_photo', models.ImageField(upload_to='image/')),
                ('email', models.CharField(max_length=50)),
                ('iletişim_tel', models.CharField(max_length=50)),
                ('kargo_adres', models.CharField(max_length=50)),
                ('kkkart_numarasi', models.CharField(max_length=30)),
                ('kkkart_ay', models.CharField(max_length=30)),
                ('kkkart_yil', models.CharField(max_length=30)),
                ('kkkart_cvv', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Yardım',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yrdm_title', models.CharField(max_length=50)),
                ('yrdm_description', models.CharField(max_length=250)),
                ('yrdm_keywords', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='site_ayarları',
            name='bizkmz_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=550),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site_ayarları',
            name='yardım_tel',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]