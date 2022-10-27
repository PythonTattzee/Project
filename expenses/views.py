from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category
from datetime import datetime, timedelta



class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            # search by date in a range where starting date is a date from the table
            # and enddate is the current date
            date = form.cleaned_data.get('name', '')
            enddate = datetime.now().strftime("%Y-%m-%d")
            if date:
                queryset = queryset.filter(date__range=(date, enddate))


        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

class SearchResultsView(ListView):
    model = Expense
    template_name = 'search_results.html'
