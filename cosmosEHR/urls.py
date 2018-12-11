from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('clinicaltools/', include('clinical.urls'), name='clinicaltools'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]
