from django.urls import path

from . import views

urlpatterns = [
    path('bills/monthly', views.get_all_monthly_bills, name='get_all_monthly_bills'),
    path('bills/monthly/<int:id>', views.get_by_id, name='get_by_id')
]
