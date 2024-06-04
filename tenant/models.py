from django.db import models
from authentication.models import Tenant

import uuid

# Create your models here.

class Swipe(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant')
    partner = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='partner', null=True, blank=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.status}] between {self.tenant} and {self.partner}'
    

class Match(models.Model):
    match_id = models.AutoField(primary_key=True, default=uuid.uuid4(), editable=False)
    tenant1 = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant1', blank=True, null=True)
    tenant2 = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant2', blank=True, null=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.status}] between {self.tenant1} and {self.tenant2}'