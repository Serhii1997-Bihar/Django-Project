# Generated by Django 5.1.1 on 2024-10-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_administrationmodel_alter_productsmodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrationmodel',
            options={'verbose_name': 'Адмін', 'verbose_name_plural': 'Адміни'},
        ),
        migrations.AlterField(
            model_name='administrationmodel',
            name='skills',
            field=models.CharField(max_length=300, verbose_name='Навички'),
        ),
    ]
