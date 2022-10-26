from django.contrib import admin
from .models import Expense
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    e_list_display = ("name", "category", "amount", "date")


admin.site.register(Expense, ExpenseAdmin)
