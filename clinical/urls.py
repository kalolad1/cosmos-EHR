from django.urls import path
from . import views

urlpatterns = [
    path('store-variants/', views.store_variants, name='clinical/store-variants'),
    path('', views.home, name='clinical/home'),
    path('patient_story/<int:patient_id>/', views.patient_story, name='clinical/patient-story'),
    path('create-patient/', views.create_patient, name='clinical/create-patient'),
    path('entry/<int:patient_id>/', views.entry, name='clinical/entry'),
    path('variant-display/<int:patient_id>/', views.variant_display, name='clinical/variant-display'),
    path('genome-scan/<int:variant_id>/', views.genome_scan, name='clinical/genome-scan'),
]
