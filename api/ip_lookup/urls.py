from django.urls import path
from .views import all, unique

urlpatterns = [
    path("all/<str:ip>", all),
    path("unique/<str:ip>/<str:key>", unique),
]
