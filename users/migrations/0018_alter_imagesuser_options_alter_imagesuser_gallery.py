# Generated by Django 5.1.1 on 2024-10-30 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_profileuser_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesuser',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереї'},
        ),
        migrations.AlterField(
            model_name='imagesuser',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='users.galleryuser', verbose_name='Галерея'),
        ),
    ]