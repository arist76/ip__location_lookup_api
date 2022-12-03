from django.urls import path
from .views import all_view, unique_view

urlpatterns = [
    path("<str:ip>", all_view, name="all"),
    path("<str:ip>/<str:key>", unique_view, name="unique"),
]
