from django import forms
from . import models


class PetForm(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = [
            "title",
            "description",
            "image",
            "price",
        ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = [
            "description",
            "imege",
            "service_title",
        ]


class Our_teamForm(forms.ModelForm):
    class Meta:
        model = models.Our_team
        fields = [
            "full_name",
            "image",
            "age",
            "information",
        ]
