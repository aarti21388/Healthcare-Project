from django.shortcuts import render, redirect
from appointment.models import AppointmentForm, AppointmentDetails
from django.http import JsonResponse
from registration.models import Patient
from django.shortcuts import get_object_or_404
from django.contrib import messages


def appointment_form(request,id=None):
    if id is None:
        return render(request, 'appointment.html')
    
    patient=Patient.objects.get(id=id)
    print(patient.name,patient.dob,patient.id,patient.email)
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your appointment schedule successfully")
            return redirect('patient:search_patient')
        
    else:
        form=AppointmentForm(instance=patient)
        form.fields['patient_id'].initial = patient.id
    
    
    return render(request, 'appointment.html',{'form':form})


def update_model(request):
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def cancel_appointment(request, appointment_id):
    return JsonResponse({'message': 'Invalid request method.'}, status=400)
