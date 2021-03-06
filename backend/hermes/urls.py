from django.urls import path

from . import views

urlpatterns = [
    path('bills/monthly/', views.get_all_monthly_bills, name='get_all_monthly_bills'),
    path('bills/monthly/<int:id>/', views.get_by_id, name='get_by_id'),
    path('bills/payperiod/', views.get_monthly_bills_for_pay_period, name='get_monthly_bills_for_pay_period'),
    path('bills/monthly/update/<int:id>/', views.update_bill, name='update_bill')
]
