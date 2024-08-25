from django.contrib import admin
from .models import Materiel, staff , affect
from django.contrib.auth.models import Group  

admin.site.site_header = 'DBSHENCKER INVENTORY DASHBOARD'

# Register your models here.
admin.site.register(staff)
admin.site.register(Materiel)
admin.site.register(affect)

