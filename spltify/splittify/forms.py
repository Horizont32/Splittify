from django import forms
from django.core.exceptions import ValidationError

from .models import *

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = '__all__'

    def clean_payer(self):
        payer = self.cleaned_data['payer']
        trip_participants = User.objects.filter(trip=self.cleaned_data['trip'].id)
        if payer not in trip_participants:
            raise ValidationError('Wrong User picked')

        # Trip.objects.filter(users__trip=self.cleaned_data['trip'].id)
        # print(a)
        # print(self.cleaned_data['trip'].name)
        # print(payers)
        return payer

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = '__all__'

    def clean_bill_ower(self):
        bill_ower = self.cleaned_data['bill_ower']
        print(self.cleaned_data['bill'].id)
        trip_participants = User.objects.filter(trip__bill=self.cleaned_data['bill'].id)
        if bill_ower not in trip_participants:
            raise ValidationError('Wrong User picked')
        return bill_ower

