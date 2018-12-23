from django.contrib import admin
from clinical import models


admin.site.register(models.Patient)
admin.site.register(models.Variant)
admin.site.register(models.HealthEncounter)
# admin.site.register(models.Relative)
# admin.site.register(models.Disease)
# admin.site.register(models.Medication)
