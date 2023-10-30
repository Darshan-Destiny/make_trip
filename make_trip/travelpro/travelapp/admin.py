from django.contrib import admin
from .models import Destination,Package,Offer

# Register your models here.
admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Offer)