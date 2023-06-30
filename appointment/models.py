from django.db import models
from registration.models import Patient
from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms

TIME_SLOT_CHOICES = [
    ('09:00', '9:00 AM'),
    ('10:00', '10:00 AM'),
    ('11:00', '11:00 AM'),
    ('12:00', '12:00 PM'),
    ('1:00', '1:00 PM'),
    ('2:00', '2:00 PM'),
    ('3:00', '3:00 PM'),
    ('4:00', '4:00 PM'),
]

class AppointmentDetails(models.Model):
    appointment_date = models.DateField(null=True,blank=True)
    time_slot = models.CharField(max_length=8, null=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,default=True)
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField()
    email = models.CharField(max_length=255, null=True)
    doctor_name = models.CharField(max_length=255, null=True)
    purpose = models.CharField(max_length=255, null=True)
    
 
    def __str__(self):
        return f"Appointment - {self.doctor_name} - {self.name}"
    
    def clean(self):
        if self.appointment_date and self.appointment_date < timezone.now().date():
            raise ValidationError("Appointment date must be in the future.")

class AppointmentForm(forms.ModelForm):
    class Meta:
       
        model = AppointmentDetails
        fields ='__all__'
        widgets = {
            'time_slot': forms.Select(choices=TIME_SLOT_CHOICES),
            'appointment_date':forms.DateInput(attrs={'type': 'date'}),
            'patient_id':forms.TextInput(attrs={'type':'number'})
        }
        
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['appointment_date']
        
    
    
