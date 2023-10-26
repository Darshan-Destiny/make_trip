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
    no_of_day = models.IntegerField()
    price = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)

    class Meta:
        db_table = 'Package'
