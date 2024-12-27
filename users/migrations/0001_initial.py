# Generated by Django 5.1.1 on 2024-10-15 18:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(blank=True, upload_to='users_photo/gallery/', verbose_name='Галерея')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateField(blank=True, verbose_name='Народження')),
                ('photo', models.ImageField(blank=True, default='users_styles/User.png', upload_to='users_photo/', verbose_name='Основна світлина')),
                ('hobby', models.CharField(blank=True, max_length=400, verbose_name='Хоббі')),
                ('city', models.CharField(blank=True, max_length=40, verbose_name='Місто')),
                ('phone', models.IntegerField(blank=True, max_length=15, verbose_name='Телефон')),
                ('info', models.TextField(blank=True, verbose_name='Інформація')),
                ('gallery', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.galleryuser', verbose_name='Галерея')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Основний User')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
        ),
    ]