from django.contrib import admin
from .models import UserModel, VehicleDetails, Trips

# Register your models here.
admin.site.register(UserModel)
admin.site.register(VehicleDetails)
admin.site.register(Trips)