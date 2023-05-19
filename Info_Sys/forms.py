from django.forms import ModelForm
from django import forms
from .models import Resident

class ResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields = "__all__"
        labels = {
            'resID'       : 'Resident ID No.',
            'firstName'   : 'First Name',
            'lastName'    : 'Last Name',
            'middleName'  : 'Middle Name',
            'birthday'    : 'Birthday',
            'sex'         : 'Sex',
            'civilStatus' : 'Civil Status',
            'sitio'       : 'Sitio',
        }
        widgets = {
            'resID'       : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'firstName'   : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'lastName'    : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'middleName'  : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'birthday'    : forms.TextInput(attrs={'class':'form-select', 'placeholder':'yyyy-mm-dd'}),
            'sex'         : forms.Select(attrs={'class':'form-select', 'placeholder':'Sex'}),
            'civilStatus' : forms.Select(attrs={'class':'form-select', 'placeholder':'Civil Status'}),
            'sitio'       : forms.Select(attrs={'class':'form-select', 'placeholder':'Sitio'}),
        }
