# Generated by Django 5.1.1 on 2024-10-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_productsmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='about',
            field=models.TextField(blank=True, max_length=250, verbose_name='Інформація'),
        ),
    ]
