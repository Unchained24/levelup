from dataclasses import field
from django.forms import ModelForm, TextInput, widgets
from django import forms
from .models import Details

class DetailsForm(ModelForm):
    research = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Phone number, username, or email'}))
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Password'}))
    class Meta:
        model = Details
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['research'].label =''
        # self.fields['info'].label =''