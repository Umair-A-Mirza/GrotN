from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=18, null=True)
    budget = models.IntegerField(null=True)
    desiredLocation = models.CharField(max_length=100, null=True)
    roommate = models.BooleanField(null=True, default=False)
    about = models.TextField(null=True)

    def __str__(self): 
        return self.user.username + " (Tenant " + str(self.id) + ")"


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=18, null=True)
    noHouses = models.IntegerField(null=True)

    def __str__(self): 
        return self.user.username + " (Landlord " + str(self.id) + ")"
