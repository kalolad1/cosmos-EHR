from django import forms
from . import choices


class PatientForm(forms.Form):
    sex = forms.ChoiceField(choices=choices.SEX)
    race = forms.ChoiceField(choices=choices.RACE)




