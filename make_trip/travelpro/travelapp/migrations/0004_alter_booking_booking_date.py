# Generated by Django 4.2.6 on 2023-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_booking_booking_date_alter_booking_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
