from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import MonthlyBill

import json

def get_all_monthly_bills(request):

    bills = [model_to_dict(bill) for bill in MonthlyBill.objects.all()]

    return JsonResponse({'bills': bills})

def get_by_id(request, id):

    bill = MonthlyBill.objects.get(pk=id)

    return JsonResponse(model_to_dict(bill))
