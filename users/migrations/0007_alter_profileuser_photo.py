# Generated by Django 5.1.1 on 2024-10-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profileuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users_photo/', verbose_name='Основна світлина'),
        ),
    ]