from django.contrib import admin

# Register your models here.

from .models import House, Housing

admin.site.register(House)
admin.site.register(Housing)