# Generated by Django 5.1.1 on 2024-11-05 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_imagesuser_options_alter_imagesuser_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryuser',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереї'},
        ),
    ]
