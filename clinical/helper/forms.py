from django import forms
from clinical.helper import choices
from clinical.models import HealthEncounter


class PatientForm(forms.Form):
    sex = forms.ChoiceField(choices=choices.SEX)
    race = forms.ChoiceField(choices=choices.RACE)


class HealthEncounterForm(forms.ModelForm):

    class Meta:
        model = HealthEncounter
        fields = ('location', 'type_of_encounter', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
        }






