import math
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, SalarySlip  # <-- import model

@api_view(['POST'])
def calculate_salary(request):
    try:
        employee_name = request.data.get('employee_name')
        employee = Employee.objects.get(name=employee_name)
        employe_salary = int(request.data.get("salary", 0))
        employe_absents = int(request.data.get("absents", 0))
        employe_shortshift = int(request.data.get("short_shift", 0))
        employe_late = int(request.data.get("late", 0))
        employe_halfday = int(request.data.get("half_day", 0))

        number_of_days = 30
        salary_per_day = employe_salary / number_of_days

        deducation_days_of_short_shift = math.floor(employe_shortshift / 3)
        deducation_days_of_late = math.floor(employe_late / 3)

        total_absents = employe_absents + (employe_halfday * 0.5)
        total_deducation = deducation_days_of_short_shift + deducation_days_of_late

        if total_absents > 2:
            total_deducation += (total_absents - 2)

        final_salary = math.floor(employe_salary - (total_deducation * salary_per_day))

        # Save to database
        SalarySlip.objects.create(
            employee=employee,
            salary=employe_salary,
            absents=employe_absents,
            short_shift=employe_shortshift,
            late=employe_late,
            half_day=employe_halfday,
            deduction_days=total_deducation,
            final_salary=final_salary
        )

        return Response({
            "message": "Salary slip generated and saved successfully",
            "data": {
                "employee_name": employee.name,
                "employee_email": employee.email,
                "employee_phone": employee.phone,
                "employee_cnic": employee.cnic,
                "original_salary": employe_salary,
                "deduction_days": total_deducation,
                "final_salary": final_salary
            }
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
@api_view(['POST'])
def create_employee(request):
    try:
        employee = Employee.objects.create(
            name = request.data.get('name'),
            email = request.data.get('email'),
            phone = request.data.get('phone'),
            cnic = request.data.get('cnic'),
            address = request.data.get('address'),
        )
        return Response({"message": "Employee created successfully",  "id": employee.id})
    except Exception as e:
        return Response({"error": e}, status=400)
    
@api_view(['GET'])
def get_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        data = {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.cnic,
            'address': employee.address
        }
        return Response(data)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)


@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all().values()
    return Response(list(employees))

@api_view(['PUT'])
def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.name = request.data.get("name", employee.name) 
        employee.email = request.data.get("email", employee.email) 
        employee.phone = request.data.get("phone", employee.phone) 
        employee.cnic = request.data.get("cnic", employee.cnic) 
        employee.address = request.data.get("address", employee.address)
        employee.save()
        return Response({"message": "Employee Updated Successfully"}) 
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found."}, status=404)

@api_view(['DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response({"message": "Employee Deleted Successfully."})
    except Employee.DoesNotExist:
        return Response({"error": 'Employee not found.'}, status=404)
        