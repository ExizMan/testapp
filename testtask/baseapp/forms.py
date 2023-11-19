from django import forms
from .models import Employees, Professions


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['firstname', 'midname', 'lastname', 'profession']
        labels = {'firstname':'Имя', 'midname':'Отчество', 'lastname':'Фамилия', 'profession':'Должность'}

