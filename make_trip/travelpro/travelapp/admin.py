from django.contrib import admin
from .models import Destination,Package,Offer,Booking,Payment,Contact,Customer,Shop,Order,OrderItem,ShippingAddress

# Register your models here.
admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Offer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

