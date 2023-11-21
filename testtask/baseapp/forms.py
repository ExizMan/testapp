import re
from django import forms
from .models import Employees, Professions
from django.core.exceptions import ValidationError


class EmployeeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['profession'].empty_label = "Выберете профессию"
    class Meta:
        model = Employees
        fields = ['firstname', 'midname', 'lastname', 'profession']
        labels = {'firstname': 'Имя', 'midname': 'Отчество(необязательно)', 'lastname':'Фамилия', 'profession': 'Должность'}

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        if bool(re.search('[A-Za-z0-9,./<>?;:{}\[\]]', firstname)):
            raise forms.ValidationError("Используйте только кириллицу")

        if bool(re.search(r'\s', firstname)):
            raise forms.ValidationError("Пишите все в правильных полях")
        return firstname.title()
    def clean_midname(self):
        midname= self.cleaned_data['midname']
        if midname is None:
            return None
        if bool(re.search('[A-Za-z0-9,./<>?;:{}\[\]]', midname)):
            raise forms.ValidationError("Используйте только кириллицу")
        if bool(re.search(r'\s', midname)):
            raise forms.ValidationError("Пишите все в правильных полях")
        return midname.title()

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        if bool(re.search(r'[A-Za-z0-9,./<>?;:{}\[\]]', lastname)):
            raise forms.ValidationError("Используйте только кириллицу")
        if bool(re.search(r'\s', lastname)):
            raise forms.ValidationError("Пишите все в правильных полях")
        return lastname.title()


class ProfessonsForm(forms.ModelForm):
    class Meta:
        model = Professions
        fields = ['tittle']
        labels = {'tittle': 'Должность'}

    def clean_tittle(self):
        tittle = self.cleaned_data['tittle']
        if bool(re.search(r'[<>?;:{}\[\]]', tittle)):
            raise forms.ValidationError("Вы используете какие-то подозрительные символы :/")
        return tittle

