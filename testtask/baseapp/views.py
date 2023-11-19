from django.shortcuts import render, redirect
from .models import Employees,Professions
from django.views.generic.base import View


def employees(request):
    employees = Employees.objects.order_by()
    context = {'employees' : employees}
    return render(request, 'baseapp/employees.html', context)

def professions(request):
    professions = Professions.objects.all()
    context = {'professions' : professions}
    return render(request, 'baseapp/professions.html', context)
# Create your views here.
