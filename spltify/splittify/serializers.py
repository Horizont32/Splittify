from rest_framework import serializers
from .models import *


class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'