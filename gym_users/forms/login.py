from django import forms
from gym_users.models import User


class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password']
