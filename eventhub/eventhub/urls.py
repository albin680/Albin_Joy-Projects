from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Standard Django Admin
    path('admin/', admin.site.urls),
    
    # Core App URLs (Home, Search, Bookings, Auth, etc.)
    # Ensure your app name is 'core' or change this to match your app's directory name
    path('', include('core.urls')),
]

# Serving Media and Static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)