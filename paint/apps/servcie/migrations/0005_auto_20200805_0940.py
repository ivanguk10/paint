# Generated by Django 3.0.4 on 2020-08-05 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servcie', '0004_remove_service_service_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='price',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='service',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='subservice',
            name='slug',
        ),
    ]
