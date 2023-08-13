from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ['email', 'password', 'type', 'birth_date']
    TYPE_CHOICES = [("coach", 'COACH'), ("user", 'USER')]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['type'] = 'datetime'
        self.fields['birth_date'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'


        self.fields['type'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        exists= User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("Email Alreayt Exists")
        return True