# Generated by Django 4.2.6 on 2023-11-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_alter_booking_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='new',
            field=models.CharField(default='dinner', max_length=20),
        ),
    ]
