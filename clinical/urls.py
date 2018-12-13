from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='clinical/home'),
    path('create-patient/', views.create_patient, name='create-patient'),
    path('entry/<int:patient_id>/', views.entry, name='clinical/entry'),
    path('variant-display/<int:patient_id>/', views.variant_display, name='clinical/variant-display'),
    path('genome-scan/<int:variant_id>/', views.genome_scan, name='clinical/genome-scan'),

    path('store-variants/', views.store_variants, name='clinical/store-variants'),
]
