from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date


class UserSignUpForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    father_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password', 'type', 'birth_date','first_name', 'last_name', 'father_name']

    TYPE_CHOICES = [("coach", 'COACH'), ("user", 'USER')]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['type'] = 'datetime'
        self.fields['birth_date'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'

        self.fields['type'].widget.attrs['class'] = 'form-control'

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #
    #     exists = User.objects.filter(email=email).exists()
    #     print(email, 'email', exists)
    #     if exists:
    #         raise forms.ValidationError("Email Alreayt Exists")
    #     return True

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 18 and self.cleaned_data.get('type') == 'coach':
            raise forms.ValidationError("Coaches must be 18 or older.")
        return birth_date
