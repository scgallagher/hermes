from django.http import JsonResponse, HttpResponse
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

def update_bill(request, id):

    body = request.body.decode('utf-8')
    new_bill = json.loads(body)
    print(new_bill.get('name'))

    current_bill = MonthlyBill.objects.get(pk=id)
    current_bill.name = new_bill.get('name')
    current_bill.due_date = new_bill.get('due_date')
    current_bill.amount = new_bill.get('amount')
    current_bill.type = new_bill.get('type')
    current_bill.auto_pay = new_bill.get('auto_pay')

    current_bill.save()

    return HttpResponse(status=200)
