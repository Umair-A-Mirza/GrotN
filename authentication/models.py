from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    accountCreated = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=18, null=True)
    budget = models.IntegerField(null=True)
    desiredCity = models.CharField(max_length=100, null=True)
    desiredDistrict = models.CharField(max_length=100, null=True)
    roommate = models.BooleanField(null=True, default=False)
    activities = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    preferences = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        about = ""
        about += f"Likes {self.activities}. " if self.activities else ""
        about += f"Interested in {self.interests}. " if self.interests else ""
        about += f"Prefers {self.preferences}. " if self.preferences else ""
        self.about = about.strip()
        return super(Tenant, self).save(*args, **kwargs)


    def __str__(self): 
        return self.user.username + " (Tenant " + str(self.id) + ")"


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=18, null=True)
    noHouses = models.IntegerField(null=True)
    baseCity = models.CharField(max_length=100, null=True)
    additionalInfo = models.TextField(null=True, blank=True)

    def __str__(self): 
        return self.user.username + " (Landlord " + str(self.id) + ")"
