from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Bill)
admin.site.register(Trip)
admin.site.register(Transactions)
admin.site.register(SplitWays)