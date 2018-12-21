from django.contrib import admin
from .models import Patient, Variant, HealthEncounter


admin.site.register(Patient)
admin.site.register(Variant)
admin.site.register(HealthEncounter)
