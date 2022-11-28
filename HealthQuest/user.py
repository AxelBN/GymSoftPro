from django import forms
from .models import HealthQuests

class Users(forms.ModelForm):
    class Meta:
        model = HealthQuests
        fields = '__all__'