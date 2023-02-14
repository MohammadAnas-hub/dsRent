from django.contrib import admin
from .models import UserModel, Service, SubServices, VehicleDetails, Bookings

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Service)
admin.site.register(SubServices)
admin.site.register(VehicleDetails)
admin.site.register(Bookings)