from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class UserModel(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=250)   #while taking it as an input in forms we will use PasswordInput on form
    phone = models.BigIntegerField(blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    userImg = models.ImageField(upload_to='accounts/images', null=True, blank=True)
    licenseNumber = models.CharField(max_length=20)
    dob = models.DateTimeField()
    city = models.CharField(max_length=40)
    # userType = models.CharField(max_length=50)
    # desc = models.TextField(null=True)
    # verified = models.BooleanField(default=False)
    # online = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class ForgetPassword(models.Model):
    user = models.ForeignKey('UserModel', related_name='userforgetpassword', on_delete=models.CASCADE)
    token = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.token

class Service(models.Model):
    serviceId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serviceName = models.CharField(max_length=50)

    def __str__(self):
        return self.serviceName

class SubServices(models.Model):
    subServiceId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subServiceName = models.CharField(max_length=50)
    parentService = models.ForeignKey('Service', related_name='parentService', on_delete=models.CASCADE)

    def __str__(self):
        return self.subServiceName


class VehicleDetails(models.Model):
    vehicleDetailsID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehChoices = (('Sedan', 'Sedan'),
                   ('SUV', 'SUV'),
                   ('Van', 'Van'),
                   ('Luxury', 'Luxury'),
                   ('Bus', 'Bus'))
    vehicleCategory = models.CharField(max_length=20, choices=vehChoices)
    vehicleBrand = models.CharField(max_length=30)
    vehicleModel = models.CharField(max_length=30)
    vehicleModelYear = models.IntegerField()
    vehiclePlateNo = models.CharField(max_length=30)
    corrServiceId = models.ForeignKey('Service', related_name='corrServiceId', on_delete=models.CASCADE)
    city = models.CharField(max_length=40)
    # branchId -----------------------------------------(foreign key)
    vehiclephoto = models.ImageField(upload_to='accounts/images', null=True, blank=True)
    document = models.ImageField(upload_to='accounts/images', null=True, blank=True)
    # driver = models.ForeignKey('Driver', related_name='driver', on_delete=models.CASCADE)
    totalBookings = models.IntegerField(default=0)
    vehicleColor = models.CharField(max_length=30, blank=True)
    seatCapacity = models.IntegerField()




    # what to do with this

    # assigned = models.BooleanField(default=False)
    # def nowAssigned(self):
    #     self.assigned = True

    def __str__(self):
        return self.vehicleCategory


class Bookings(models.Model):
    tripId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # sourceId = models.ForeignKey()
    date = models.DateField()
    time = models.TimeField()
    bookedServiceId = models.ForeignKey('Service', related_name='bookedService', on_delete=models.CASCADE)
    bookedSubServiceId = models.ForeignKey('SubServices', related_name='bookedSubServiceId', on_delete=models.CASCADE)
    pCity = models.CharField(max_length=40)
    pAddress = models.CharField(max_length=100)
    pDate = models.DateField()
    pTime = models.TimeField()
    dCity = models.CharField(max_length=40)
    dAddress = models.CharField(max_length=100)
    dDate = models.DateField()
    dTime = models.TimeField()
    bookedUserId = models.ForeignKey('UserModel', related_name='bookedUser', on_delete=models.CASCADE)
    bookedVehicleId = models.ForeignKey('VehicleDetails', related_name='bookedVehicleId', on_delete=models.CASCADE)
    # bookedDriverId = models.ForeignKey('VehicleDetails', related_name='bookedVehicleId', on_delete=models.CASCADE)
    price = models.IntegerField()
    paymentStatus = models.BooleanField(default=False)
    remarks = models.IntegerField()

    def __str__(self):
        return self.time