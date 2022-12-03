from django.urls import path
from .views import full_ip_location_data_endpoint, unique_ip_location_data_endpoint

urlpatterns = [
    path("<str:ip>", full_ip_location_data_endpoint, name="all"),
    path("<str:ip>/<str:key>", unique_ip_location_data_endpoint, name="unique"),
]
