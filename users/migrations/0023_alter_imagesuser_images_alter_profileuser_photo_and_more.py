# Generated by Django 5.1.1 on 2024-12-12 16:44

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_galleryuser_date_remove_galleryuser_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesuser',
            name='images',
            field=models.ImageField(blank=True, upload_to=users.models.PathMedia.user_images, verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to=users.models.PathMedia.user_avatar, verbose_name='Основна світлина'),
        ),
        migrations.AlterField(
            model_name='videosuser',
            name='videos',
            field=models.FileField(blank=True, upload_to=users.models.PathMedia.user_videos, verbose_name='Відео'),
        ),
    ]
