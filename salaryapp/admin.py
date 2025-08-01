from django.contrib import admin
from .models import Employee, SalarySlip

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cnic', 'address')

@admin.register(SalarySlip)
class SalarySlipAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'absents', 'short_shift', 'late', 'half_day', 'deduction_days', 'final_salary', 'created_at')
