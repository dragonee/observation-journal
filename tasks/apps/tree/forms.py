from django import forms

from .models import Observation, Thread


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name']


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = [
            "situation", "interpretation", "approach", "pub_date", "type", "date_closed"
        ]