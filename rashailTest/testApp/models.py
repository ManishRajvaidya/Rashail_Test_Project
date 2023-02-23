import uuid
from django.db import models

# Create your models here.

class Machine(models.Model):

    machine_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_name  = models.CharField(max_length = 200, default = 'default_machine')

    def __str__(self):
        return self.machine_name + " ---> " + str(self.machine_id)

class Patient(models.Model):

    patient_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    patient_name  = models.CharField(max_length = 200, default = 'default_patient')

    def __str__(self):
        return self.patient_name + " ---> " + str(self.patient_id)

class Dose(models.Model):

    dose_id = models.AutoField(primary_key=True)
    dose = models.FloatField(max_length=25, blank=False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dose) + " ---> dose_id: " + str(self.dose_id)
