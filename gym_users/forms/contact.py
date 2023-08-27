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

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'


