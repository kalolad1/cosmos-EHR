from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Base paths
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='home'),

    # App specific paths
    path('clinical/', include('clinical.urls'), name='clinical'),
    path('accounts/', include('accounts.urls'), name='accounts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
