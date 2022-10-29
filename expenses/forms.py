from django import forms
from .models import Expense
from .models import Category


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False

class CategoriesSearchForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

    name = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name='name',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

