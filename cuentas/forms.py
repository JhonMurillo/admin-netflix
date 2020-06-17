from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from django.contrib.auth.models import User
from django.db import transaction
from users.models import Profile
from cuentas.models import Account, AccountDetail
import datetime


class CreateAccountForm(forms.Form):
    """Create Account form."""
    email = forms.EmailField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70
    )

    pay_value = forms.DecimalField(min_value=0, decimal_places=2, max_digits=8)
    active_at = forms.DateField(initial=datetime.date.today)
    expire_at = forms.DateField(initial=datetime.date.today)

    def clean_email(self):
        """Username must be unique."""
        email = self.cleaned_data['email']
        email_taken = Account.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email ya fue registrado.')
        return email

    def clean_expire_at(self):
        """Verify password confirmation match."""
        data = super().clean()
        if data['expire_at'] < data['active_at']:
            raise forms.ValidationError('Fecha de expiración no puede ser menor a la fecha de activacion.')
        return data

    def save(self):
        """Create Account"""
        try:
            with transaction.atomic():
                data = self.cleaned_data
                print(data) 
                account = Account(
                    email=data['email'],
                    password=data['password']
                )

                account_detail = AccountDetail(
                    account=account,
                    pay_value=data['pay_value'],
                    active_at=data['active_at'],
                    expire_at=data['expire_at']
                )
                account.save()
                account_detail.save()
        except Exception as ex:
            print(ex)
            raise ValidationError(ex)



class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()