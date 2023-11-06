from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

class Destination(models.Model):
    country_name = models.CharField(max_length=20)
    location_name = models.CharField(max_length=30)
    image = models.FileField()

    class Meta:
        db_table = 'Destination'


class Package(models.Model):
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE,null=True,default=None)
    image = models.FileField()
    location_name = models.CharField(max_length=20)
    people = models.IntegerField()
    no_of_day = models.CharField(max_length=20)
    no_of_night = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    tour_guide = models.CharField(max_length=20,default='1')
    insurance = models.CharField(max_length=20,default='1')
    tax = models.CharField(max_length=20,default='1')
    total_cost1 = models.IntegerField(default='0')
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


class Payment(models.Model):



    name = models.CharField(max_length=20)
    email = models.EmailField(default='.com',blank=True,null=True)
    number = models.IntegerField(default='00')
    card_name = models.CharField(max_length=20,default='visa')
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2,null=True)
    year = models.CharField(max_length=2,default='23')
    cvv_code = models.CharField(max_length=3,null=True)
    country = models.CharField(max_length=20,default='india')
    street1 = models.CharField(max_length=50,default='fdfd')
    street2 = models.CharField(max_length=50,default='fdfdf')
    city = models.CharField(max_length=20,default='ff')
    state = models.CharField(max_length=15,default='gujarat')
    postal_code = models.CharField(max_length=4,default='01')
    add_information = models.CharField(max_length=200,default='hello')



    class Meta:
        db_table = 'Payment'






class Booking(models.Model):





    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(
                _("%(value)s is not an even number"),
                params={"value": value},
            )




    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,null=True,blank=True)
    package = models.ForeignKey(Package,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=20)
    new = models.CharField(max_length=20,default='dinner')
    email = models.EmailField()
    number = models.IntegerField(validators=[validate_even])
    option = (('tour_guide','tour_guide'),
                  ('insurance', 'insurance'),
                  ('dinner','dinner'),
                  ('bike_rent','bike_rent'),)
    select = models.CharField(max_length=10,choices=option,default='dinner')
    booking_date = models.DateField(default=datetime.now())





    class Meta:
        db_table = 'Booking'




class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    class Meta:
        db_table = 'Contact'




