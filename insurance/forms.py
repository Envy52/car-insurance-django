from django import forms
from .models import Insurance
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = [
            'car_model', 'policy_number',
            'insurance_date', 'expiry_date','company',
            'amount_paid',
        ]

