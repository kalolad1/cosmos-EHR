from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinicaltools),
    path('patient/', views.patient),
    path('patient/entry/', views.entry),
    path('patient/entry/processing', views.processing),
    path('patient/entry/scan/<int:chrom>/<int:pos>/<str:ref>/<str:alt>/', views.scan, name='scan'),
]
