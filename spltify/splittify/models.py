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

    class Meta:
        verbose_name_plural = "SplitWays"

    def __str__(self):
        return f'{self.split_by}'


class Bill(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_is_payer')
    way_to_split = models.ForeignKey(SplitWays, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    total_amount = models.IntegerField()  # this is the sum of all amounts in transactions table
    owers = models.ManyToManyField(User, through="Transactions", related_name='user_is_ower')

    def __str__(self):
        return f'{self.name} bill payed by {self.payer} for {self.total_amount} coins'


class Transactions(models.Model):

    class Meta:
        verbose_name_plural = "Transactions"

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    bill_ower = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'trip__users': True})
    amount = models.IntegerField()
    completion = models.BooleanField()

    def __str__(self):
        return f'{self.bill_ower.username} owes {self.amount} by bill {self.bill.name} to {self.bill.payer}'
