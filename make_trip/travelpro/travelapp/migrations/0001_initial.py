# Generated by Django 4.2.6 on 2023-11-06 09:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import travelapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
                ('location_name', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'Destination',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_percentage', models.CharField(max_length=10)),
                ('image', models.FileField(upload_to='')),
                ('country_name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
                ('real_price', models.CharField(max_length=20)),
                ('cut_of_price', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Offer',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, default='.com', max_length=254, null=True)),
                ('number', models.IntegerField(default='00')),
                ('card_name', models.CharField(default='visa', max_length=20)),
                ('card_number', models.CharField(max_length=16)),
                ('month', models.CharField(max_length=2, null=True)),
                ('year', models.CharField(default='23', max_length=2)),
                ('cvv_code', models.CharField(max_length=3, null=True)),
                ('country', models.CharField(default='india', max_length=20)),
                ('street1', models.CharField(default='fdfd', max_length=50)),
                ('street2', models.CharField(default='fdfdf', max_length=50)),
                ('city', models.CharField(default='ff', max_length=20)),
                ('state', models.CharField(default='gujarat', max_length=15)),
                ('postal_code', models.CharField(default='01', max_length=4)),
                ('add_information', models.CharField(default='hello', max_length=200)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('location_name', models.CharField(max_length=20)),
                ('people', models.IntegerField()),
                ('no_of_day', models.CharField(max_length=20)),
                ('no_of_night', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('tour_guide', models.CharField(default='1', max_length=20)),
                ('insurance', models.CharField(default='1', max_length=20)),
                ('tax', models.CharField(default='1', max_length=20)),
                ('total_cost1', models.IntegerField(default='0')),
                ('desc', models.CharField(max_length=100)),
                ('detail_desc', models.CharField(max_length=500)),
                ('destination', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='travelapp.destination')),
            ],
            options={
                'db_table': 'Package',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('new', models.CharField(default='dinner', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField(validators=[travelapp.models.Booking.validate_even])),
                ('select', models.CharField(choices=[('tour_guide', 'tour_guide'), ('insurance', 'insurance'), ('dinner', 'dinner'), ('bike_rent', 'bike_rent')], default='dinner', max_length=10)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travelapp.package')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travelapp.payment')),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]
