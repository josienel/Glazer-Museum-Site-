from django.contrib import admin
from .models import Activity, Play, Exhibit, Connection
import os
import sys

# Add the Django project's root directory to the Python path
sys.path.append('/Users/danny/Desktop/Django/DjangoProject')

admin.site.register(Activity)    
admin.site.register(Play)
admin.site.register(Exhibit)
admin.site.register(Connection)


# Register your models here.
