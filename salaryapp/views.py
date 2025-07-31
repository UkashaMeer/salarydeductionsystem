import math
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def calculate_salary(request):
    try:
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

        return Response({
            "final_salary": final_salary,
            "deduction_days": total_deducation
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)
