from django.contrib import admin
from testApp.models import Machine, Patient, Dose

# Register your models here.

admin.site.register(Machine)
admin.site.register(Patient)
admin.site.register(Dose)