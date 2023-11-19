from django import forms
from gym_users.models import User, Payments
from django.contrib.auth.forms import UserCreationForm


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['Address'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
