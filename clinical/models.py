from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from clinical.helper import constants, choices


class Patient(models.Model):
    # For current implementation, each patient is associated with exactly one physician.
    physician = models.ForeignKey(User, on_delete=models.CASCADE)

    # Demographic information
    # The following fields are required to filled out by the user.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=50, choices=choices.SEX)

    # The following fields are optional and MAY be filled out by the user.
    email = models.CharField(max_length=75, blank=True)
    address = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=50, choices=choices.RACE, blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True)

    # The following fields are calculated without user input.
    date_created = models.DateField(default=timezone.now)

    # This field stores genome wide information. Currently,
    # a directory with separate chromosome-level nucleotide sequence files
    # should be uploaded.
    genome = models.FileField(upload_to='genomes/', blank=True)

    def full_name(self):
        """
        Returns the full name of the patient.

        Returns:
            string: The full name of the patient.
        """
        return self.first_name + " " + self.last_name

    def __str__(self):
        """
        Returns the string representation of the patient object.

        Returns:
            string: Full ame of the patient.
        """
        return self.full_name()

    def get_age(self):
        """
        Calculates the age of the patient based on their date of birth.

        Returns:
            int: The age of the patient.
        """
        days_old = (date.today() - self.date_of_birth).days
        return days_old // 365

    def date_of_first_visit_formatted(self):
        """
        Formats the date of the patients first visit in a readable way.

        Returns:
            string: The date of the first visit.
        """
        return self.date_created.strftime("%b %e %Y'")


class Variant(models.Model):
    gene_id = models.CharField(max_length=50)
    gene_name = models.CharField(max_length=100)
    phenotype_list = models.CharField(max_length=200)
    start = models.IntegerField()
    stop = models.IntegerField()
    clinical_significance = models.CharField(max_length=200)
    chromosome = models.IntegerField()
    reference_allele = models.CharField(max_length=1)
    alternate_allele = models.CharField(max_length=1)

    def __str__(self):
        """
        Returns a string representation of a Variant object.

        Returns:
             string: String containing the gene name of the variant.
        """
        return self.gene_name

    def related_diagnosis(self):
        """
        Returns the diagnosis related to the variant object.

        Returns:
             string: String representation of a diagnosis
        """
        for diagnosis, gene in constants.DIAGNOSES_TO_GENE.items():
            if self.gene_id == gene:
                return diagnosis
        return "No diagnosis available"

    @staticmethod
    def retrieve_variants_from_diagnosis_list(d_list):
        """
        Finds all relevant variants from a list of diagnoses.

        Params:
            d_list: A string containing comma separated diagnoses.

        Returns:
             QuerySet: A set of Variant objects which are relevant to all the diagnoses.
        """
        # Creates an array of diagnoses.
        d_list_array = d_list.split(', ')

        # Retrieves all relevant gene_IDS from DIAGNOSES_TO_GENE_MAPPING dictionary.
        gene_IDs = [constants.DIAGNOSES_TO_GENE[i] for i in d_list_array if i in constants.DIAGNOSES_TO_GENE]

        # Retrieves all Variant objects associated with the genes in genes_IDs.
        relevant_variants = Variant.objects.filter(gene_id__in=gene_IDs)

        return relevant_variants


class HealthEncounter(models.Model):
    # Parties involved.
    physician = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Logistical information.
    date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)
    type_of_encounter = models.CharField(max_length=100, choices=choices.TYPE_OF_HEALTH_ENCOUNTER)

    # Content.
    # TODO Placeholder description field
    description = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of a HealthEncounter object.

        Returns:
             string: The patient name, physician name, and date.
        """
        return self.patient.full_name() + " with " + self.physician.username + " on " + self.date_formatted()

    def date_formatted(self):
        """
        Formats the date of the Health Encounter in a readable way.

        Returns:
            string: The date of the Health Encounter.
        """
        return self.date.strftime("%b %e %Y")

    def he_type_fa_icon(self):
        """
        Returns the fa icon name according to the health encounter type.

        Returns:
            string: Fa icon name.
        """
        return choices.HE_TO_ICON[self.type_of_encounter]
















