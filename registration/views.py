from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime
from .models import Patient
from django.contrib import messages


def registration_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact_details = form.cleaned_data['contact_details']
            dob = form.cleaned_data['dob']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            medical_history =form.cleaned_data['medical_history']
            
            if Patient.objects.filter(contact_details=contact_details).exists():
                error_message='Contact details already Registered'
                return render(request,'registration.html',{'form':form,'error_message':error_message})
            form.save()
            messages.success(request,"Registration Successful Thank you for registering. ")
            return redirect('patient:search_patient')
        else:
            return render(request, 'registration.html', {'form': form, 'error_message': 'Invalid form data.'})
    
    else:
        form=RegistrationForm()
        return render(request, 'registration.html',{'form':form})


def home(request):
    return render(request, 'home.html')
