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