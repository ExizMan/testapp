from django import forms
from .models import Employees, Professions
from django.core.exceptions import ValidationError
lat = 'qwertyuioasdfghjklzxcvbnm'
tags = r'[];'""',./'

class EmployeeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['profession'].empty_label = "Выберете профессию"
    class Meta:
        model = Employees
        fields = ['firstname', 'midname', 'lastname', 'profession']
        labels = {'firstname':'Имя', 'midname':'Отчество', 'lastname':'Фамилия', 'profession':'Должность'}

    def clean_title(self):
        # cleaned_data = super(EmployeeForm, self).clean()
        # firstname = cleaned_data.get("firstname")
        # midname = cleaned_data.get("midname")
        # lastname = cleaned_data.get("lastname")
        # if lat in firstname:
        #     raise ValidationError("Используйте только латиницу")
        # if lat in midname:
        #     raise ValidationError("Используйте только латиницу")
        # if lat in lastname:
        #     raise ValidationError("Используйте только латиницу")
        # if tags in firstname:
        #     raise ValidationError("Не используйте теги")
        # if tags in midname:
        #     raise ValidationError("Не используйте теги")
        # if tags in lastname:
        #     raise ValidationError("Не используйте теги")


