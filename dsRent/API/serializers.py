from rest_framework import serializers
from .models import UserModel, ForgetPassword, Service, SubServices, VehicleDetails, Bookings


# serializer for user Model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

# Serializer for ForgetPasswordSerializer
class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetPassword
        fields = '__all__'


# Serializer for Service Class
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ServiceSerializer, self).__init__(*args, **kwargs)


# SubService Serializer Class
class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServices
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(SubServiceSerializer, self).__init__(*args, **kwargs)

# Vehicle Class Serializer
class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'

    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(VehicleDetailsSerializer, self).__init__(*args, **kwargs)


# Booking Class Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'

    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(BookingSerializer, self).__init__(*args, **kwargs)


# Registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('userId', 'firstName', 'lastName', 'password', 'phone', 'email', 'userImg', 'licenseNumber', 'dob', 'city')