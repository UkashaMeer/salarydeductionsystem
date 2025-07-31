from django.urls import path
from .views import calculate_salary

urlpatterns = [
    path('calculate-salary/', calculate_salary),
]
