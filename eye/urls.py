from django.urls import path

from . import views

urlpatterns = [
    path(r'event/<int:application_id>', views.event)
]