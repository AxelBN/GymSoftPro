from django import forms
from .models import physical_evaluation

class pe(forms.ModelForm):
    class Meta:
        model = physical_evaluation
        fields = '__all__'