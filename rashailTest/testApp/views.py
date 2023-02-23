from django.shortcuts import render
from django.http import JsonResponse
from testApp.serializers import DoseSerializer
from testApp.models import Dose, Machine, Patient

def index(request):
    return render(request, 'index.html')

def last_dose(request, machine_id):
    if request.method == 'GET':

        try:
            patients = Patient.objects.filter(machine_id_id = machine_id).values()

            dose_details = []
            for patient in patients:

                patient_id = str(patient.get("patient_id"))
                doses = Dose.objects.filter(patient_id_id = patient_id).values()

                if doses != []:
                    for dose in doses:
                        dose_details.append(dose)

            last_dose_id = 0
            for dose in dose_details:
                if dose.get("dose_id") > last_dose_id:
                    last_dose_id = dose.get("dose_id")

            required_last_dose = Dose.objects.filter(dose_id = last_dose_id)
            serial_dose = DoseSerializer(required_last_dose, many=True)
            return JsonResponse({"success": "true", "last dose": serial_dose.data[0].get("dose")}, safe=False)
        
        except IndexError:
            return JsonResponse({"success": "true", "message": "No dose available for this machine id"})
        
        except Exception as e:
            return JsonResponse({"success": "false", "message": str(e)})
        
        

def last_dose_from_html(request):
    if request.method == 'GET':

        try:
            machine_id = request.GET.get("machine_id")
            patients = Patient.objects.filter(machine_id_id = machine_id).values()

            dose_details = []
            for patient in patients:

                patient_id = str(patient.get("patient_id"))
                doses = Dose.objects.filter(patient_id_id = patient_id).values()

                if doses != []:
                    for dose in doses:
                        dose_details.append(dose)

            last_dose_id = 0
            for dose in dose_details:
                if dose.get("dose_id") > last_dose_id:
                    last_dose_id = dose.get("dose_id")

            required_last_dose = Dose.objects.filter(dose_id = last_dose_id)
            serial_dose = DoseSerializer(required_last_dose, many=True)
            return JsonResponse({"success": "true", "last dose": serial_dose.data[0].get("dose")}, safe=False)
        
        except IndexError:
            return JsonResponse({"success": "true", "message": "No dose available for this machine id"})
        
        except Exception as e:
            return JsonResponse({"success": "false", "message": str(e)})