from django.db import models

# Create your models here.

class Destination(models.Model):
    country_name = models.CharField(max_length=20)
    location_name = models.CharField(max_length=30)
    image = models.FileField()

    class Meta:
        db_table = 'Destination'


class Package(models.Model):
    image = models.FileField()
    location_name = models.CharField(max_length=20)
    people = models.IntegerField()
    no_of_day = models.CharField(max_length=20)
    no_of_night = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    detail_desc = models.CharField(max_length=500)

    class Meta:
        db_table = 'Package'

class Offer(models.Model):
    off_percentage = models.CharField(max_length=10)
    image = models.FileField()
    country_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    real_price = models.CharField(max_length=20)
    cut_of_price = models.CharField(max_length=20)

    class Meta:
        db_table = 'Offer'


class Booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    date = models.DateField()
    phone = models.IntegerField()
    booking_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'Booking'

class Payment(models.Model):
    name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    amount = models.IntegerField()
    package_cost = models.IntegerField()
    dedicated_tour_guide = models.IntegerField()
    insurance_cost = models.IntegerField()
    tax = models.IntegerField()
    total_cost = models.IntegerField()

    class Meta:
        db_table = 'Payment'


class BillingAddress(models.Model):
    country = models.CharField(max_length=20)
    street1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    postal_code = models.IntegerField()
    add_information = models.CharField(max_length=200)

    class Meta:
        db_table = 'BillingAddress'


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    class Meta:
        db_table = 'Contact'




