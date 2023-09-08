from django.contrib import admin
from .models import *
# Register your models here.

class TransactionsAdmin(admin.ModelAdmin):
	list_display = ('bill_ower', 'amount')


admin.site.register(Bill)
admin.site.register(Trip)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(SplitWays)