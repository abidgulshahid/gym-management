from django import forms
from gym_users.models import User


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'type']
    TYPE_CHOICES = [("coach", 'COACH'), ("user", 'USER')]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists= User.objects.filter(email__iexact=email)
        if exists:
            raise forms.ValidationError("Email Alreayt Exists")
        return True



