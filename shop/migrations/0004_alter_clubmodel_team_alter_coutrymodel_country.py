# Generated by Django 5.1.1 on 2024-10-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_clubmodel_team_alter_coutrymodel_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmodel',
            name='team',
            field=models.CharField(max_length=30, null=True, verbose_name='Клуб'),
        ),
        migrations.AlterField(
            model_name='coutrymodel',
            name='country',
            field=models.CharField(max_length=30, null=True, verbose_name='Країна'),
        ),
    ]
