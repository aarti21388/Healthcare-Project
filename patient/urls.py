from django.contrib import admin
from django.urls import include, path, re_path
from . import views


app_name = 'patient'

urlpatterns = [

    #path('home/',views.allpatient,name='allpatient'),
    path('', views.search_patient, name="search_patient"),
    path('<int:patient_id>/', views.patient_details, name="patient_details"),
    path('edit/<int:pk>/', views.update_patient, name='edit'),
    path('appointments/<int:patient_id>/',
         views.appointments, name='appointments'),
    path('appointment/reschedule/<int:patient_id>/',
         views.reschedule_appointment, name='reschedule_appointment'),
    path('notes/view/<int:patient_id>/', views.getNotesByPatientId,
         name='noteDetail'),
    path('notes/add/<int:patient_id>/', views.addNotesByPatientId,
         name='addNote'),
]
