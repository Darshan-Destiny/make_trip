# Generated by Django 4.2.6 on 2023-11-06 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0009_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 6, 10, 26, 23, 417606)),
        ),
    ]
