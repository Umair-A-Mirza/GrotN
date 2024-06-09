from django.db import models

# Create your models here.

class House(models.Model):
    house_id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=400, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    square_meters = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    hosting_roommates = models.BooleanField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    available = models.BooleanField(null=True, blank=True)
    landlord = models.ForeignKey('authentication.Landlord', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.address if self.address else 'House ' + str(self.house_id)
    

class Housing(models.Model):
    match_id = models.AutoField(primary_key=True, unique=True, editable=False)
    tenants = models.ForeignKey('tenant.Match', on_delete=models.CASCADE, null=False)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=False)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    paid1 = models.BooleanField(default=False)
    paid2 = models.BooleanField(default=False)

    # TODO: find a proper representation for Housing objects
    def __str__(self):
        return str(self.match_id)