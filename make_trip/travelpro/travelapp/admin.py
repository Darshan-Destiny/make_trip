from django.contrib import admin
from .models import Destination,Package,Offer,Booking,Payment

# Register your models here.
admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Offer)
admin.site.register(Booking)
admin.site.register(Payment)
