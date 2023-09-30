from django import forms
from gym_users.models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date
import re


class UserSignUpForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    father_name = forms.CharField(max_length=255)
    cnic = forms.CharField(max_length=255)
    gender = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    mobile_no = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['cnic', 'email', 'password', 'type',
                  'birth_date', 'first_name',
                  'last_name', 'father_name', 'gender', 'address', 'mobile_no' ]

    TYPE_CHOICES = [("coach", 'COACH'), ("user", 'USER')]
    GENDER = [("MALE", 'MALE'), ("FEMALE", 'FEMALE')]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES)
        self.fields['gender'] = forms.ChoiceField(choices=self.GENDER)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['cnic'].widget.attrs['placeholder'] = '123456789111'
        self.fields['birth_date'].widget.attrs['type'] = 'datetime'
        self.fields['birth_date'].widget = forms.TextInput(attrs={'type': 'date'})


        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'

        self.fields['cnic'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_no'].widget.attrs['class'] = 'form-control'

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 18 and self.cleaned_data.get('type') == 'coach':
            raise forms.ValidationError("Coaches must be 18 or older.")
        return birth_date

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        print(first_name)
        regex = r'^[a-zA-Z]*$'
        print(re.search(regex, first_name))
        if first_name and not re.search(regex, first_name):
            raise forms.ValidationError("Only Alphabets are allowed")
        return first_name

    def clean_last_name(self):
        first_name = self.cleaned_data['last_name']
        print(first_name)
        regex = r'^[a-zA-Z]*$'
        print(re.search(regex, first_name))
        if first_name and not re.search(regex, first_name):
            raise forms.ValidationError("Only Alphabets are allowed")
        return first_name

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        print(mobile_no)

        if mobile_no and len(mobile_no) <=14 and len(mobile_no) > 10:
            return mobile_no
        raise forms.ValidationError("Minimum 11 Digit Required  ")


    def clean_cnic(self):
        cnic = self.cleaned_data['cnic']
        if Profile.objects.filter(cnic=cnic).exists():
            raise forms.ValidationError("Cnic Already Exists")
        elif len(cnic) < 13:
            raise forms.ValidationError("CNIC must be atleast 13 Digits")
        return cnic




