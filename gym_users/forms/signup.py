from django import forms
from gym_users.models import User


class UserSignUpForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password', 'type']
    TYPE_CHOICES = [("coach", 'coach'), ("user", 'user')]

    def __init__(self, user, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['type'].choices = self.TYPE_CHOICES

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists= User.objects.filter(email__iexact=email)
        if exists:
            raise forms.ValidationError("Email Alreayt Exists")
        return True



