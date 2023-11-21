from django import forms
from gym_users.models import User, Payments, Profile
from django.contrib.auth.forms import UserCreationForm


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)



