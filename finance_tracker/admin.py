from django.contrib import admin

# Register your models here.
from finance_tracker.models import *

# Models
admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Currency)
admin.site.register(Reminder)
admin.site.register(Budget)
admin.site.register(Account)
admin.site.register(Category)
