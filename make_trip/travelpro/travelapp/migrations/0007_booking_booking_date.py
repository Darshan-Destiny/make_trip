# Generated by Django 4.2.6 on 2023-11-06 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_remove_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 11, 6, 10, 23, 49, 336333), null=True),
        ),
    ]
