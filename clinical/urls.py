from django.urls import path
from . import views

urlpatterns = [
    path('store-variants/', views.store_variants, name='clinical/store-variants'),
    path('', views.home, name='clinical/home'),
    path('create-patient/', views.create_patient, name='clinical/create-patient'),

    path('patient-story/<int:patient_id>/', views.patient_story, name='clinical/patient-story'),
    path('patient-story-basic/', views.patient_story_basic, name='clinical/patient-story-basic'),

    path('add-health-encounter/<int:patient_id>', views.add_health_encounter, name='clinical/add-health-encounter'),
    path('health-encounter-view/<int:health_encounter_id>', views.health_encounter_view, name='clinical/health-encounter-view'),

    path('entry/<int:patient_id>/', views.entry, name='clinical/entry'),
    path('variant-display/<int:patient_id>/', views.variant_display, name='clinical/variant-display'),
    path('genome-scan/<int:variant_id>/', views.genome_scan, name='clinical/genome-scan'),

    # Testing paths
    path('test-html/', views.test_html, name='clinical/test_html')
]
