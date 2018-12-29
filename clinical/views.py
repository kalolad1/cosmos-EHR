from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, HealthEncounter


@login_required
def home(request):
    """
    This view sends the user home with all of their stored patients.
    """
    # Retrieves all of the users patients from the database.
    all_patients = Patient.objects.filter(physician=request.user)
    return render(request, 'clinical/home.html', {'patients': all_patients})


@login_required
def create_patient(request):
    # If a user tries to create a new patient.
    if request.method == 'POST':
        try:
            # Retrieve all of the user input and check for an error.
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            date_of_birth = request.POST['date-of-birth']
            sex = request.POST['sex']
            race = request.POST['race']
            genome = request.FILES['genome']
        except KeyError:
            return render(request, 'clinical/create-patient.html', {'error': 'Select fields needed!'})

        # Store the patient object in the database.
        patient = Patient(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                          sex=sex, race=race, genome=genome, physician=request.user)
        email = request.POST['email']
        address = request.POST['address']
        patient.email = email if email else ""
        patient.address = address if address else ""
        patient.save()
        return redirect('clinical/home')

    # Bring the user to the create-patient page.
    return render(request, 'clinical/create-patient.html')


@login_required
def health_story(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'clinical/health-story/home.html', {'patient': patient})



