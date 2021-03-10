from datetime import date

from django.db import models
from rest_framework.exceptions import ValidationError

policy_choices = [('MI', 'Motor Insurance'), ('TI', 'Travel Insurance'), ('HI', 'Home Insurance'),
                  ('PI', 'Property Insurance'), ('PA', 'Personal Accident'),
                  ('WLI', 'Whole Life Insurance')]


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('DOB cannot be in the future.')


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(validators=[no_future])
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'
        ordering = ['-created_at']


class Insurance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=policy_choices)
    premium = models.PositiveBigIntegerField(blank=False, null=False)
    cover = models.PositiveBigIntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'insurance'
        unique_together = ['customer', 'type']
        ordering = ['-created_at']
