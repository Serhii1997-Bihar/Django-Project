# Generated by Django 5.1.1 on 2024-10-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_clientdata_address_alter_clientdata_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата формування'),
        ),
    ]
