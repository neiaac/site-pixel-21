from .views import video
from django.urls import path, include

from home import views

urlpatterns = [
    path('', video),
]
