# Generated by Django 5.0.3 on 2024-03-12 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2024, 3, 12)),
        ),
    ]