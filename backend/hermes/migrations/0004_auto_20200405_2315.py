# Generated by Django 3.0.4 on 2020-04-05 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0003_monthlybill_auto_pay_enabled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlybill',
            old_name='auto_pay_enabled',
            new_name='auto_pay',
        ),
    ]