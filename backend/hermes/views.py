from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import MonthlyBill

import json

def get_all_monthly_bills(request):

    bills = [populate_bill_to(bill) for bill in MonthlyBill.objects.all()]

    return JsonResponse({'bills': bills})

def get_monthly_bills_for_pay_period(request):

    body = request.body.decode('utf-8')
    request_body = json.loads(body)

    pay_period_start = request_body.get('payPeriodStart')
    pay_period_end = request_body.get('payPeriodEnd')

    print(type(pay_period_start))

    bills = MonthlyBill.objects.filter(due_date__gte=pay_period_start).filter(due_date__lte=pay_period_end)

    totalAmountDue = sum([bill.amount for bill in bills])

    bills = [populate_bill_to(bill) for bill in bills]

    response = {
        'bills': bills,
        'totalAmountDue': totalAmountDue
    }

    return JsonResponse(response)

def get_by_id(request, id):

    bill = MonthlyBill.objects.get(pk=id)

    return JsonResponse(populate_bill_to(bill))

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

    return HttpResponse(status=204)

def populate_bill_to(bill):

    return {
        'id': bill.id,
        'name': bill.name,
        'amount': bill.amount,
        'type': bill.type,
        'dueDate': bill.due_date,
        'autopay': bill.auto_pay
    }
