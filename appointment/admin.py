from django.contrib import admin
from .models import AppointmentDetails
from registration.models import Patient
from django import forms 

@admin.register(AppointmentDetails)
class AppointmentDetailsAdmin(admin.ModelAdmin):
    #list_display = ['doctor_name', 'patient_id', 'appointment_date', 'time_slot']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'patient_id':
            kwargs['queryset'] = Patient.objects.only('id')
            kwargs['widget'] = forms.TextInput(attrs={'type': 'number'})
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
