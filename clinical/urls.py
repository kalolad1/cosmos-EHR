from django.urls import path
from . import views

urlpatterns = [
    # Base paths.
    path('', views.home, name='clinical/home'),
    path('create-patient/', views.create_patient, name='clinical/create-patient'),

    # View a patient story.
    path('health-story/<int:patient_id>/', views.health_story, name='clinical/health-story'),
]
