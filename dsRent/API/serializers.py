from rest_framework import serializers
from .models import UserModel



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)