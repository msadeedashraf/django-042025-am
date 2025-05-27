from django import forms
from . import models


class CreateJob(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = [
            "title",
            "location",
            "company",
            "jobtype",
            "description",
            "applylink",
        ]
