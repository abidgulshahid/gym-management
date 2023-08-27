from django import forms
from gym_users.models import User, Payments
from django.contrib.auth.forms import UserCreationForm


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ['bank_account_number', 'zip', 'Address', 'amount']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['zip'].widget.attrs['class'] = 'form-control'
        self.fields['Address'].widget.attrs['class'] = 'form-control'
        self.fields['bank_account_number'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
