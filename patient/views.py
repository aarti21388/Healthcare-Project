from appointment.models import AppointmentForm, AppointmentDetails
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from registration.models import Patient, Notes
from django.shortcuts import get_object_or_404
from appointment.models import AppointmentDetails,TIME_SLOT_CHOICES
from registration.forms import RegistrationForm,Noteform
from django.contrib  import messages



def allpatient(request):
    patient=Patient.objects.all()
    if patient:
        return render(request,'search-patient.html',{'patient':patient})
    else:
        return render(request,'search-patient.html')
    
def search_patient(request):
    
    name=request.GET.get('name')
    if name is not None:
        patient=Patient.objects.filter(Q(name__icontains=name) | Q(email__icontains=name) | Q(address__icontains=name) )
        paginator=Paginator(patient,1)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        print(page_obj)
        return render(request, 'search-patient.html',{'patient':patient,'search_name':name,'page_obj':page_obj})
    else:
        return render(request,'search-patient.html')


def patient_details(request, patient_id):
    patient=Patient.objects.get(id=patient_id)
    print(patient)
    return render(request, 'patient-details.html',{'patient':patient})


def update_patient(request, pk):
    patient=get_object_or_404(Patient,id=pk)
    
    if request.method=='POST':
        form=RegistrationForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request,'Patient details updateded successfully!')
            return redirect('patient:patient_details',patient_id=patient.id)
          
    else:
        form=RegistrationForm(instance=patient)
    return render(request, 'update-patient.html',{'patient':form})


def appointments(request, patient_id):
    patient=get_object_or_404(Patient,id=patient_id)
    if patient:
        appointment=AppointmentDetails.objects.filter(patient_id=patient_id)
        return render(request,'list_appointment.html',{'appointment':appointment})
    

def reschedule_appointment(request, patient_id): 
    appointment=get_object_or_404(AppointmentDetails,id=patient_id)

    if request.method=='POST':
        form=AppointmentForm(request.POST,instance=appointment)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            
            messages.success(request,"Appointment reschedule successfully")
            print(form)
            return redirect('patient:patient_details',patient_id=appointment.patient_id.id)
    else:
        form=AppointmentForm(instance=appointment)
        print(appointment.patient_id)
    return render(request, 'update-appointment.html',{'form':appointment,'timeslot':TIME_SLOT_CHOICES})



def getNotesByPatientId(request, patient_id):
    notes=Notes.objects.filter(patient=patient_id)
    
    if notes:
        #patient_id=notes[0].patient.id
        return render(request, 'notes-page.html',{'notes':notes,'patient_id':patient_id})
    return render(request, 'notes-page.html',{'patient_id':patient_id})


def addNotesByPatientId(request, patient_id):
    patient=Patient.objects.get(id=patient_id)
    if request.method =='POST':
        content = request.POST['content']
        patient=patient
        note=Notes(content=content,patient=patient)
        note.save()
        return redirect('patient:noteDetail', patient_id=patient_id)
    else:                                                                            
        return render(request,"add-notes.html")

