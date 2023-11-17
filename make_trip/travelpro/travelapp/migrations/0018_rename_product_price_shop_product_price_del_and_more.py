# Generated by Django 4.2.6 on 2023-11-08 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0017_customer_order_alter_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='product_price',
            new_name='product_price_del',
        ),
        migrations.AddField(
            model_name='shop',
            name='product_price_org',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 8, 9, 20, 18, 134635)),
        ),
    ]
