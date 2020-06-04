from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from . import mixins

# Create your views here.
class IndexView(generic.ListView):
    model = Day
    paginate_by = 3

    def get_context_data(self):
        #テンプレートへ渡す辞書の作成
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        #テンプレートへ渡す「employee_list」を作成
        form = SearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset().order_by('-date') #データの一覧を取得

        #絞り込み
        weather = form.cleaned_data['weather'] 
        if weather:
            queryset = queryset.filter(weather=weather)
        return queryset


"""
def index(request):
    context = {
        'day_list':Day.objects.all(),
    }
    return render(request, 'employee/day_list.html', context)
"""

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy("employee:index")

"""
def add(request):

    form = DayCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employee:index')
    
    context = {
        'form': form
    }
    return render(request, 'employee/day_form.html', context)
"""

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('employee:index')


"""
def update(request, pk):
    day = get_object_or_404(Day, pk=pk)

    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employee:index')
    
    context = {
        'form': form
    }
    return render(request, 'employee/day_form.html', context)
"""

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:index')

"""
def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('employee:index')
    
    context = {
        'day': day,
    }
    return render(request, 'employee/day_confirm_delete.html', context)
"""

"""
class DetailView(generic.DetailView):
    model = Day

"""

def detail(request, pk):
    day = get_object_or_404(Day, pk=pk)
    comments = Comment.objects.filter(day=day)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.day = day
            comment.save()
    else:
        form = CommentForm()
    print
    context = {
        'day': day,
        'form': form,
        'comments': comments
    }
    return render(request, 'employee/day_detail.html', context)

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'employee/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context