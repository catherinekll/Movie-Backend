# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Movie

# create a ModelForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


# class PersonForm(forms.ModelForm):
#    class Meta:
#        model = Person
#        fields = "__all__"
