# Generated by Django 3.0.4 on 2020-08-03 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servcie', '0002_subservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservice',
            name='service_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Цена услги'),
        ),
    ]
