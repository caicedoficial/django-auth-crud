from django import forms
from .models import Tasks

class TaksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'descripcion', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la descrición de la tarea'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }