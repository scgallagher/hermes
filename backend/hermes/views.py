from django.http import JsonResponse
from django.core import serializers
from .models import MonthlyBill

import json

def get_all_monthly_bills(request):

    bills = serializers.serialize('json', MonthlyBill.objects.all())
    bills = json.loads(bills)
    bills = [bill.get('fields') for bill in bills]

    print(bills[0])

    return JsonResponse({'bills': bills})
