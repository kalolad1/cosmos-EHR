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
            string: Full name of the patient.
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

#
# class Medication(models.Model):
#     # TODO a set of names, only, pull from some database
#     name = models.CharField(max_length=100)
#
#     # TODO make more structured
#     doses = models.CharField(max_length=100)
#     refill = models.CharField(max_length=100)
#     instructions = models.CharField(max_length=100)
#
#     def __str__(self):
#         """
#         Returns the string representation of the Medication object.
#
#         Returns:
#             string: Name of the medication.
#         """
#         return self.name
#
#
# class Disease(models.Model):
#     name = models.CharField(max_length=100)
#     chronic_condition = models.BooleanField(default=False)
#
#     # TODO currently a char field, but change to something more structured
#     prognosis = models.CharField(max_length=50, blank=True)
#
#     related_medications = models.ManyToManyField(Medication)
#     time_of_diagnosis = models.DateField(default=timezone.now)
#
#     def __str__(self):
#         """
#         Returns the string representation of the Disease object.
#
#         Returns:
#             string: Name of the disease.
#         """
#         return self.name
#
#
# # Todo Make a Person super class
# class Relative(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#
#     date_of_birth = models.DateField()
#     date_of_death = models.DateField(null=True, blank=True)
#     diseases = models.ManyToManyField(Disease)
#
#     relationship = models.CharField(max_length=50, choices=choices.RELATIONSHIP)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#
#     # TODO Make it a Foreign Key to Disease?
#     cause_of_death = models.CharField(max_length=50, blank=True)
#
#     def __str__(self):
#         """
#         Returns the string representation of the Relative object.
#
#         Returns:
#             string: Full name of the relative.
#         """
#         return self.full_name()
#
#     def full_name(self):
#         """
#         Returns the full name of the relative.
#
#         Returns:
#             string: The full name of the relative.
#         """
#         return self.first_name + " " + self.last_name


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
















