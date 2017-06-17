from django import forms

from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name', 'last_name', 'phone_number', 'work_place', 'company', 'e_mail')
