# Generated by Django 3.2.18 on 2023-05-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_sepetim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sepetim',
            old_name='total_fiyat',
            new_name='total_atted',
        ),
    ]