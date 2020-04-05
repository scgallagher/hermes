from django.db import models

class MonthlyBill(models.Model):

    name = models.CharField(max_length=200)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    type = models.CharField(max_length=200)
    auto_pay = models.BooleanField(default=False)

    def __str__(self):
        return self.name