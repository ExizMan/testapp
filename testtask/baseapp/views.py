from django.shortcuts import render, redirect, get_object_or_404
from .models import Employees,Professions
from .forms import EmployeeForm
from django.views.generic.base import View


def index(request):
    return render(request, 'baseapp/index.html')
def employees(request):
    employees = Employees.objects.order_by()
    context = {'employees' : employees}

    return render(request, 'baseapp/employees.html', context)

def professions(request):
    professions = Professions.objects.all()
    context = {'professions': professions}
    return render(request, 'baseapp/professions.html', context)

def employee(request, emp_id):
    employee = Employees.objects.get(id=emp_id)
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
        sublabel = 'ждем изменений'
    else:
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save()
            sublabel = 'изменения приняты'


    context = {'form': form, 'employee':employee, 'sublabel':sublabel}
    return render(request, 'baseapp/employee.html',context)

def new_employee(request):
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baseapp:employees')
    context = {'form': form}
    return render(request,'baseapp/new_employee.html', context)
def del_employee(request,emp_id):
    model = get_object_or_404(Employees,id=emp_id)
    if request.method == 'POST':
        employee.delete()
    return


def test(request, emp_id):
    employee = Employees.objects.get(id=emp_id)
    context = {'employee':employee}
    return render(request, 'baseapp/test.html')
# Create your views here.
