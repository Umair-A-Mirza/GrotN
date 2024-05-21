from django.db import models

# Create your models here.

class House(models.Model):
    house_id = models.AutoField(primary_key=True, unique=True, editable=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    square_feet = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(null=True, blank=True)
    landlord = models.ForeignKey('authentication.Landlord', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.address
    

class Match(models.Model):
    match_id = models.AutoField(primary_key=True, unique=True, editable=False)
    tenant = models.ForeignKey('authentication.Tenant', on_delete=models.CASCADE, null=False)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=False)
    approved = models.BooleanField(default=False)
    is_active = models.BooleanField(efault=True)

    def __str__(self):
        return self.tenant + ' ' + self.house