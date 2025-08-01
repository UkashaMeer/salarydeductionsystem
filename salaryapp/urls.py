from django.urls import path
from .views import calculate_salary, create_employee, list_employees, update_employee, delete_employee, get_employee

urlpatterns = [
    path('calculate-salary/', calculate_salary),
    path('employees/', list_employees),
    path('employees/create', create_employee),
    path('employees/update/<int:pk>/', update_employee),
    path('employees/delete/<int:pk>/', delete_employee),
    path('employees/<int:pk>/', get_employee),
]
