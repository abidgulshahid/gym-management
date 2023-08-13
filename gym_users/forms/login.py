from django import forms
from gym_users.models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists= User.objects.filter(email=email)
        if not exists:
            raise forms.ValidationError("Email Doesn't Exists")
        return True

