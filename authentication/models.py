from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.IntegerField(null=True)
    desiredLocation = models.CharField(max_length=100, null=True)
    roommate = models.BooleanField(null=True)
    about = models.TextField(null=True)

    def __str__(self): 
        return self.user.username + " (Tenant " + str(self.id) + ")"


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    noHouses = models.IntegerField(null=True)

    def __str__(self): 
        return self.user.username + " (Landlord " + str(self.id) + ")"
