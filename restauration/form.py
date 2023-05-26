from django import forms
from .models import Newsletter

class FormulaireNewsletter(forms.ModelForm):
    class Meta:

        model = Newsletter
        fields = ['email']