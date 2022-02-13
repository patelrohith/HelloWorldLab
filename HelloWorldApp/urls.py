
from django.urls import path
from .views import mainJsonResponse

urlpatterns = [
    path("", mainJsonResponse, name="home"),
]