from django import forms
from .models import payments

class Payments (forms.ModelForm):
    class Meta:
        model = payments
        fields = '__all__'