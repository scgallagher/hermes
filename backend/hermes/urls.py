from django.urls import path

from . import views

urlpatterns = [
    path('bills/monthly', views.get_all_monthly_bills, name='get_all_monthly_bills')
]
