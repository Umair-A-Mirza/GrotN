from django.contrib import admin

# Register your models here.

from .models import Swipe
from .models import Match

admin.site.register(Swipe)
admin.site.register(Match)