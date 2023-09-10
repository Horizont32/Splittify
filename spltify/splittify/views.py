from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import BillsSerializer, TransactionsSerializer


# Create your views here.

class BillsAPIView(viewsets.ModelViewSet):

    queryset = Bill.objects.all()
    serializer_class = BillsSerializer


# class TransactionsAPIView(generics.ListAPIView):
class TransactionsAPIView(viewsets.ModelViewSet):

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer