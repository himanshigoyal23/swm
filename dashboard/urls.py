from django.urls import path
from .views import Dashboard
from .models import mmrda1

urlpatterns = [
    path('', Dashboard, name='dashboard')
]
