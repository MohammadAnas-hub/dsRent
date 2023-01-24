from rest_framework import serializers
from .models import UserModel, VehicleDetails, Trips, ForgetPassword



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetPassword
        fields = '__all__'

class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'

    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(VehicleDetailsSerializer, self).__init__(*args, **kwargs)

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'

    # For partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(TripsSerializer, self).__init__(*args, **kwargs)
