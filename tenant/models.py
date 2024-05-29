from django.db import models
from authentication.models import Tenant

# Create your models here.

class Match(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant1')
    tenant_status = models.BooleanField(default=False)
    partner = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant2', null=True, blank=True)
    partner_status = models.BooleanField(null=True, blank=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       self.status = self.tenant_status and self.partner_status
       return super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return f'[{self.status}] between {self.tenant} and {self.partner}'