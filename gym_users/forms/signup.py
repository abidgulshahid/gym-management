from django import forms
from gym_users.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date


class UserSignUpForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    father_name = forms.CharField(max_length=255)
    cnic = forms.CharField(max_length=255)
    gender = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    memebership_date = forms.DateTimeField(initial=datetime.now())
    gym_time = forms.TimeField()
    mobile_no = forms.CharField(max_length=255)
    experience = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['cnic', 'email', 'password', 'type',
                  'birth_date', 'first_name',
                  'last_name', 'father_name', 'gender', 'address', 'memebership_date', 'gym_time', 'mobile_no', 'experience' ]

    TYPE_CHOICES = [("coach", 'COACH'), ("user", 'USER')]
    GENDER = [("MALE", 'MALE'), ("FEMALE", 'FEMALE')]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES)
        self.fields['gender'] = forms.ChoiceField(choices=self.GENDER)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['type'] = 'datetime'
        self.fields['birth_date'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['memebership_date'].widget.attrs['class'] = "form-control mydatepicker"
        self.fields['gym_time'].widget = forms.TextInput(attrs={'type': 'time'})


        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'

        self.fields['cnic'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['memebership_date'].widget.attrs['class'] = 'form-control'
        self.fields['gym_time'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_no'].widget.attrs['class'] = 'form-control'
        self.fields['experience'].required = False

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
