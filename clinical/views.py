from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Variant, HealthEncounter
from clinical.helper import variant_parsing_script, genome_scanner
from .forms import HealthEncounterForm
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def home(request):
    """
    This view sends the user home with all of their stored patients.
    """
    # Retrieves all of the users patients from the database.
    all_patients = Patient.objects.filter(physician=request.user)
    return render(request, 'clinical/home.html', {'patients': all_patients})


@login_required
def patient_story(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    health_encounters = HealthEncounter.objects.filter(patient=patient)

    return render(request, 'clinical/patient-story.html', {'patient': patient,
                                                           'health_encounters': health_encounters})


@login_required
def add_health_encounter(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        form = HealthEncounterForm(request.POST)

        if form.is_valid():
            encounter = form.save(commit=False)
            encounter.patient = patient
            encounter.physician = request.user
            encounter.save()
            return HttpResponseRedirect(reverse('clinical/patient-story', args=(patient_id,)))
        else:
            error = 'Please fill out all of the fields.'
            return render(request, 'clinical/add-health-encounter.html/' + patient_id, {'error': error})

    else:
        form = HealthEncounterForm()
        return render(request, 'clinical/add-health-encounter.html', {'patient': patient, 'form': form})

@login_required
def health_encounter_view(request, health_encounter_id):
    health_encounter = HealthEncounter.objects.get(id=health_encounter_id)
    return render(request, 'clinical/health-encounter-view.html', {'health_encounter': health_encounter})


def store_variants(request):
    """
    This allows all the variants to be uploaded into the database. Should only be used once, or
    when new variants are added.
    """
    variant_parsing_script.store_all_variant_samples()
    return render(request, 'homepage.html')


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
def entry(request, patient_id):
    # Gets the relevant patient.
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'clinical/entry.html', {'patient': patient})


@login_required
def variant_display(request, patient_id):
    # Retrieve input from user.
    patient = Patient.objects.get(id=patient_id)
    diagnosis_list = request.POST['diagnosis-list']

    # Retrieves all of the relevant variants based on the diagnosis list.
    variants = Variant.retrieve_variants_from_diagnosis_list(diagnosis_list)
    return render(request, 'clinical/variant-display.html', {'patient': patient, 'variants': variants})


@login_required
def genome_scan(request, variant_id):
    # Scans the genome to check for an SNP.
    variant = Variant.objects.get(id=variant_id)
    scan = genome_scanner.GenomeScanner(variant)

    # The following code determines the line number in a text file we can find our sequence at.
    # This computation is necessary because text file search functionality does not support
    # queries which wrap from one line to the other.
    line_num = (variant.start // 50) + 2
    positions_from_end = ((variant.start / 50) - (variant.start // 50)) * 50.0
    print("Line number: " + str(line_num))
    print("Positions from beg: " + str(int(round(positions_from_end))))
    print("Sequence: " + scan.proximate_sequence)
    print("SNP Location Nucleotide: " + scan.nucleotide_at_position)

    return render(request, 'clinical/genome-scan.html', {'variant': variant,
                                                         'nucleotide_at_position': scan.nucleotide_at_position,
                                                         'snp_exists': scan.snp_exists,
                                                         'proximate_sequence_front': scan.proximate_sequence_front,
                                                         'proximate_sequence_back': scan.proximate_sequence_back})
