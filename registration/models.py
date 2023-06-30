from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender'),
    )
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=10, null=True, unique=True)
    dob = models.DateField(blank=True,null=True)
    email = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255, null=True)
    medical_history = models.CharField(max_length=2000, null=True)
    
    def __str__(self):
        return self.name
    
    

class Notes(models.Model):
    content = models.CharField(max_length=255, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
