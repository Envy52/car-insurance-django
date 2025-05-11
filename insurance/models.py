from django.db import models
from django.contrib.auth.models import User

class Insurance(models.Model):
    COMPANY_CHOICES = [
        ('INSON', 'INSON'),
        ('UzInsurance', 'UzInsurance'),
        ('KapitalSugurta', 'Kapital Sugurta'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insurances')
    car_model = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    insurance_date = models.DateField()
    expiry_date = models.DateField()
    company = models.CharField(max_length=50, choices=COMPANY_CHOICES)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_model} ({self.policy_number})"
