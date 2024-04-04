from django.contrib import admin
from .models import Employee,Upload
# Register your models here.
admin.site.register(Employee)
admin.site.register(Upload)

# makemigrations -- query create
# migrate      -- query fie
# python -m pip install pilllow -- for imagefield