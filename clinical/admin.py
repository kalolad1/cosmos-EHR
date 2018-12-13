from django.contrib import admin
from .models import Patient
from .models import Variant

admin.site.register(Patient)
admin.site.register(Variant)

