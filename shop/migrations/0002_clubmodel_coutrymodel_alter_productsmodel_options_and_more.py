# Generated by Django 5.1.1 on 2024-10-03 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(blank=True, max_length=30, verbose_name='Клуб')),
            ],
        ),
        migrations.CreateModel(
            name='CoutryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=30, verbose_name='Країна')),
            ],
        ),
        migrations.AlterModelOptions(
            name='productsmodel',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='position',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='shop.clubmodel', verbose_name='Клуб'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='shop.coutrymodel', verbose_name='Країна'),
        ),
    ]