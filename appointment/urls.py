from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'appointment'

urlpatterns = [
    path('schedule/<int:id>/', views.appointment_form, name="schedule"),
    path('update_appointment/', views.update_model, name="update_appointment"),
    path('cancel_appointment/<int:appointment_id>/',
         views.cancel_appointment, name="cancel_appointment"),
]
