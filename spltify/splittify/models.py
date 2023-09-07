from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class SplitWays(models.Model):
    split_by = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.split_by}'


class Bill(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Payer')
    way_to_split = models.ForeignKey(SplitWays, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    total_amount = models.IntegerField()  # this is the sum of all amounts in transactions table
    owers = models.ManyToManyField(User, through="Transactions", related_name='Ower')

    def __str__(self):
        return f'{self.name} bill, {self.payer=}, {self.total_amount=}'


class Transactions(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    bill_ower = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    completion = models.BooleanField()

    def __str__(self):
        return f'{self.bill_ower=} owes {self.amount=} by bill {self.bill.name}'
