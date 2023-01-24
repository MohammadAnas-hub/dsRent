from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class UserModel(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=250)   #while taking it as an input in forms we will use PasswordInput on form
    phone = models.BigIntegerField(blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    userImg = models.ImageField(upload_to='accounts/images', null=True, blank=True)
    userType = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    verified = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class ForgetPassword(models.Model):
    user = models.ForeignKey('UserModell', related_name='userforgetpassword', on_delete=models.CASCADE)
    token = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.token

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

# class HourleyService(models.Model):
#     hourleyService_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     city = models.CharField()
#     pickUpPoint = models.CharField()
#     dropOfCity = models.CharField()
#     dropOfPoint = models.CharField(blank=True)
#     datetime = models.DateTimeField(default=timezone.now)
#     noOfHours = models.IntegerField()
#     noOfGuests = models.IntegerField(blank=True)
#     noOfLuggage = models.IntegerField(blank=True)

#     def __str__(self):
#         return self.

# class CityToCityTrip(models.Model):
#     cityToCityTrip = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     city = models.CharField()
#     pickUpPoint = models.CharField()
#     dropOfCity = models.CharField()
#     dropOfPoint = models.CharField(blank=True)
#     datetime = models.DateTimeField(default=timezone.now)
#     noOfGuests = models.IntegerField(blank=True)
#     noOfLuggage = models.IntegerField(blank=True)

#     # def __str__(self):
#     #     return self.

# class LimousineService(models.Model):
#     hourleyService = models.ForeignKey('HourleyService', related_name="hourleySerive", on_delete=models.CASCADE, null=True)
#     cityToCityTrip = 

class VehicleDetails(models.Model):
    vehicleDetailsID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    driver = models.ForeignKey('UserModel', related_name='driver', on_delete=models.CASCADE)
    vehicleCategory = models.CharField(max_length=50)
    vehicleBrand = models.CharField(max_length=30)
    vehicleModel = models.CharField(max_length=30)
    vehicleModelYear = models.IntegerField()
    vehiclePlateNo = models.CharField(max_length=30)
    assigned = models.BooleanField(default=False)

    def nowAssigned(self):
        self.assigned = True

    def __str__(self):
        return self.vehicleCategory

class Trips(models.Model):
    tripsId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serviceType = models.ForeignKey('LimousineService',related_name="serviceType", on_delete=models.CASCADE)
    tripChoices = (('ScheduleTrips', 'ScheduleTrips'),
                   ('FinishedTrips', 'FinishedTrips'),
                   ('OngoingTrips', 'OngoingTrips'),
                   ('CanceledTrips', 'CanceledTrips'))
    tripCate = models.CharField(max_length=20, choices=tripChoices)

    startingTime = None
    guestPickedUp = models.BooleanField(default=False)
    endTime = None
    
    def tripStarted(self):
        self.startingTime = models.DateTimeField(default=timezone.now)

    def guestPickedUpFunc(self):
        self.guestPickedUp = True

    def tripEnded(self):
        self.endTime = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.tripCate


class LimousineService(models.Model):
    limousineServiceId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pickUpCity = models.CharField(max_length=50)
    pickupLocation = models.CharField(max_length=100)
    destinationCity = models.CharField(max_length=50)
    destinationLocation = models.CharField(max_length=100)
    pickupDateTime = models.DateTimeField(default=timezone.now)
    noOfHours = models.IntegerField()
    noOfGuests = models.IntegerField(blank=True)
    noOfLuggage = models.IntegerField(blank=True)

    limoChoices = (('HourlyService', 'HourlyService'),
                   ('CityToCityTrip', 'CityToCityTrip'),
                   ('AirportPickUp', 'AirportPickUp'),
                   ('AirportDrops', 'AirportDrops'),
                   ('WithinCitySingleTrip', 'WithinCitySingleTrip'))
    limoServCate = models.CharField(max_length=20, choices=limoChoices)

    def __str__(self):
        return self.limoServCate
