from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def validate_username(self):
        email = self.cleaned_data.get('username')
        exists= User.objects.filter(email=email).first()
        print(exists, 'existss')
        if exists:
            print('here')
            return exists.email
        raise forms.ValidationError("Email Doesn't Exists")

