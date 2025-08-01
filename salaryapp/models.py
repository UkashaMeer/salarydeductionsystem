from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cnic = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class SalarySlip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_slips')
    salary = models.IntegerField()
    absents = models.IntegerField()
    short_shift = models.IntegerField()
    late = models.IntegerField()
    half_day = models.IntegerField()
    deduction_days = models.FloatField()
    final_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Salary Slip - {self.created_at.strftime('%Y-%m-%d')}"

