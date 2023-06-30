from django import forms
from .models import Patient,Notes

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        widgets={
            'dob':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['medical_history'].required = False

class Noteform(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = '__all__'