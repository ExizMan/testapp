from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Employees, Professions
from .forms import EmployeeForm, ProfessonsForm



def index(request):
    return render(request, 'baseapp/index.html')

# Сотрудники


def employees(request):
    employees = Employees.objects.order_by()
    context = {'employees': employees}
    return render(request, 'baseapp/employees.html', context)


def employee(request, emp_id):
    sublabel = None
    employee = Employees.objects.get(id=emp_id)
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
        sublabel = 'ждем изменений'
    else:
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save()
            sublabel = 'изменения приняты'
    if sublabel is None:
        sublabel = "Похоже, вы неправильно изменили форму"
    context = {'form': form, 'employee': employee, 'sublabel': str(sublabel)}
    return render(request, 'baseapp/employee.html', context)


def new_employee(request):
    sublabel = "Вы еще не добавили сотрудников"
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

            sublabel = f'вы добавили сотрудника {request.POST.get("lastname")}'
            #return redirect('baseapp:employees')

    if sublabel is None:
        sublabel = "Похоже, вы неправильно изменили форму"
    context = {'form': form, 'sublabel': sublabel}

    return render(request,'baseapp/new_employee.html', context)


def del_employee(request,emp_id):
    employee = Employees.objects.get(id=emp_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('baseapp:employees')
    else:
        context = {'employee' : employee}
        return render(request, 'baseapp/del_employee.html', context)


# Должности


def professions(request):
    professions = Professions.objects.all()
    context = {'professions': professions}
    return render(request, 'baseapp/professions.html', context)

def new_profession(request):
    sublabel = "Вы еще не добавили должность"
    if request.method == 'GET':
        form = ProfessonsForm()
    else:
        form = ProfessonsForm(request.POST)
        if form.is_valid():
            form.save()
        sublabel = f'вы добавили должность {request.POST.get("tittle")}'
            # return redirect('baseapp:employees')
    context = {'form': form, 'sublabel': sublabel}
    # !!!
    return render(request, 'baseapp/new_profession.html', context)


def profession(request, prof_id):
    profession = Professions.objects.get(id=prof_id)
    if request.method == 'GET':
        form = ProfessonsForm(instance=profession)
        sublabel = 'ждем изменений'
    else:
        form = ProfessonsForm(instance=profession, data=request.POST)
        if form.is_valid():
            form.save()
            sublabel = 'изменения приняты'
    context = {'form': form, 'profession':profession, 'sublabel':sublabel}
    return render(request, 'baseapp/profession.html', context)


def del_profession(request, prof_id):
    profession = Professions.objects.get(id=prof_id)
    sublabel =""
    if request.method == 'POST':
        try:
            profession.delete()
            return redirect('baseapp:professions')
        except IntegrityError:

            profession_default = Professions.objects.create_profession('без должности')
            profession_default.save()
            profession.delete()
            return redirect('baseapp:professions')

    else:
        context = {'profession': profession, 'sublabel':sublabel}
        return render(request, 'baseapp/del_profession.html', context)
