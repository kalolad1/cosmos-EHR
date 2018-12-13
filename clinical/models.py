from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Patient(models.Model):
    # For current implementation, each patient is associated with exactly one physician.
    physician = models.ForeignKey(User, on_delete=models.CASCADE)

    # Demographic information
    # The following fields are required to filled out by the user.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    # TODO Implement choice feature
    MALE = 'male'
    FEMALE = 'female'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField(max_length=50)
    AMERICAN_INDIAN = 'american indian'
    ALASKA_NATIVE = 'alaska native'
    WHITE = 'white'
    BLACK_OR_AFRICAN_AMERICAN = 'black or african american'
    NATIVE_HAWAIIAN = 'native hawaiian'
    PACIFIC_ISLANDER = 'pacific islander'
    HISPANIC = 'hispanic'
    TWO_OR_MORE_RACES = 'two or more races'
    ASIAN = 'asian'
    RACES = (
        (AMERICAN_INDIAN, 'American Indian'),
        (ALASKA_NATIVE, 'Alaska Native'),
        (ASIAN, 'Asian'),
        (WHITE, 'White'),
        (BLACK_OR_AFRICAN_AMERICAN, 'Black or African American'),
        (NATIVE_HAWAIIAN, 'Native Hawaiian'),
        (PACIFIC_ISLANDER, 'Pacific Islander'),
        (HISPANIC, 'Hispanic'),
        (TWO_OR_MORE_RACES, 'Two or more races'),
    )
    # TODO Implement choice feature
    race = models.CharField(max_length=50, blank=True)

    # The following fields are optional and MAY be filled out by the user.
    email = models.CharField(max_length=75, blank=True)
    address = models.CharField(max_length=200, blank=True)

    # The following fields are calculated without user input.
    date_of_first_visit = models.DateField(default=timezone.now)

    # This field stores genome wide information. Currently,
    # a directory with separate chromosome-level nucleotide sequence files
    # should be uploaded.
    genome = models.FileField(upload_to='genomes/', blank=True)

    def __str__(self):
        """
        Returns the string representation of the patient object.

        Returns:
            A string containing the name of the patient.
        """
        return self.first_name + " " + self.last_name

    def get_age(self):
        """
        Calculates the age of the patient based on their date of birth.

        Returns:
            The age of the patient as an integer.
        """
        days_old = (date.today() - self.date_of_birth).days
        return days_old // 365

    def date_of_first_visit_formatted(self):
        """
        Formats the date of the patients first visit in a readable way.

        Returns:
            The date of the first visit as a string.
        """
        return self.date_of_first_visit.strftime("%b %e %Y'")

    def full_name(self):
        """
        Returns the full name of the patient.

        Returns:
            The full name of the patient as a string.
        """
        return self.first_name + " " + self.last_name


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
             String containing the gene name of the variant.
        """
        return self.gene_name

    def related_diagnosis(self):
        """
        Returns the diagnosis related to the variant object.

        Returns:
             String representation of a diagnosis
        """
        for diagnosis, gene in DIAGNOSES_TO_GENE.items():
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
             A set of Variant objects which are relevant to all the diagnoses.
        """
        # Creates an array of diagnoses.
        d_list_array = d_list.split(', ')

        # Retrieves all relevant gene_IDS from DIAGNOSES_TO_GENE_MAPPING dictionary.
        gene_IDs = [DIAGNOSES_TO_GENE[i] for i in d_list_array if i in DIAGNOSES_TO_GENE]

        # Retrieves all Variant objects associated with the genes in genes_IDs.
        relevant_variants = Variant.objects.filter(gene_id__in=gene_IDs)

        return relevant_variants


# Constant map of diagnoses mapped to genes.
DIAGNOSES_TO_GENE = {
    "Colon Cancer": '5395',
    "Li-Fraumeni Syndrome": '7157',
    "Breast Cancer": '5892',
    "Ovarian Cancer": '5892',
    "Cardiomyopathy": "2318",
    "Myofibrillar Myopathy": "2318",
    "Alzheimer's Disease": "5664",
}








