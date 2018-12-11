from django.db import models


class DemographicData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=75, blank=True)
    address = models.CharField(max_length=200, blank=True)

    AMERICAN_INDIAN = 'american indian'
    ALASKA_NATIVE = 'alaska native'
    WHITE = 'white'
    BLACK_OR_AFRICAN_AMERICAN = 'black or african american'
    NATIVE_HAWAIIAN = 'native hawaiian'
    PACIFIC_ISLANDER = 'pacific islander'
    HISPANIC = 'hispanic'
    TWO_OR_MORE_RACES = 'two or more races'
    RACES = (
        (AMERICAN_INDIAN, 'American Indian'),
        (ALASKA_NATIVE, 'Alaska Native'),
        (WHITE, 'White'),
        (BLACK_OR_AFRICAN_AMERICAN, 'Black or African American'),
        (NATIVE_HAWAIIAN, 'Native Hawaiian'),
        (PACIFIC_ISLANDER, 'Pacific Islander'),
        (HISPANIC, 'Hispanic'),
        (TWO_OR_MORE_RACES, 'Two or more races'),
    )
    race = models.CharField(
        max_length=50,
        choices=RACES,
        blank=True
    )

    MALE = 'male'
    FEMALE = 'female'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField(
        max_length=6,
        choices=SEX,
    )


class Patient(models.Model):
    # Relationships
    # DemographicData
    demographic_data = models.OneToOneField(
        DemographicData,
        primary_key=True,
        on_delete=models.CASCADE
    )




