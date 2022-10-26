from django.contrib import admin
from .models import Expense
from .models import Category
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    e_list_display = ("name", "category", "amount", "date")


class CategoryAdmin(admin.ModelAdmin):
    c_display = "name"


admin.site.register(Expense, ExpenseAdmin)


admin.site.register(Category, CategoryAdmin)
