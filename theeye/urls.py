from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('eye/', include('eye.urls')),
    path('admin/', admin.site.urls),
]
