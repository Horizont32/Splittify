from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.

class TransactionsAdmin(admin.ModelAdmin):
    form = TransactionForm
    list_display = ('bill_ower', 'amount')


class BillAdmin(admin.ModelAdmin):
    form = BillForm


admin.site.register(Bill, BillAdmin)
admin.site.register(Trip)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(SplitWays)
