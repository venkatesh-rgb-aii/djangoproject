from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    moviename=forms.CharField()
    hero=forms.CharField()
    heroine=forms.CharField()
    rating = forms.IntegerField()
    releaseyear=forms.IntegerField()

    class Meta():
        model=Movies
        fields = '__all__'