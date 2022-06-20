from django.contrib import admin
from django.urls import path, include


API_PATTERNS = [
    path('', include('items.urls')),
    path('', include('orders.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(API_PATTERNS)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
