from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data.get('username')
        exists= User.objects.filter(email=email).exists()
        print(exists)
        if exists:
            print('here')
            return True
        raise forms.ValidationError("Email Doesn't Exists")

