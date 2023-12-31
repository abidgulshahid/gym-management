import re

from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm
from gym_users.models import ContactForm


class Contact(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'message', 'email']

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        for field in self.fields:
            # self.fields[field].widget.attrs['class'] = "form-control"
            self.fields[field].required = True

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Please Enter Your Name'
        self.fields['message'].widget.attrs['placeholder'] = 'Please Enter Your Message'
        self.fields['email'].widget = forms.EmailInput()
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Please Enter Your Email'



    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            regex = r"[A-Za-z\s]+"
            if name and not re.search(regex, name):
                raise forms.ValidationError("Only Alphabets are allowed")
            return name
