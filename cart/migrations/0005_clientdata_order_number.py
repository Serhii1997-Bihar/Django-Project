# Generated by Django 5.1.1 on 2024-10-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_clientdata_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdata',
            name='order_number',
            field=models.PositiveIntegerField(default=0, editable=False, unique=True),
        ),
    ]
