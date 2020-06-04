from django import forms
from .models import *


class WeatherForm(forms.Form):
    weather = forms.ModelChoiceField(queryset=Weather.objects, label='天気', required=False)

class SearchForm(forms.Form):
    weather = forms.ModelChoiceField(queryset=Weather.objects, label='天気  ', required=False)

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(DayCreateForm, self).__init__(*args, **kwargs)
        self.fields['attach'].required = False

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text', 'created_at',)
