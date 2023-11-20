from django.urls import path
from . import views

app_name = 'baseapp'
urlpatterns = [
    path('', views.index, name="index"),

    # Сотрудники
    path('employees', views.employees, name='employees'),
    path('employees/<int:emp_id>/', views.employee, name="employee"),
    path('employees/<int:emp_id>/delete', views.del_employee, name="del_employee"),
    path('employees/new_employee/', views.new_employee, name="new_employee"),

    # Должности
    path('professions', views.professions, name='professions'),
    path('professions/<int:prof_id>/', views.profession, name="profession"),
    path('professions/<int:prof_id>/delete', views.del_profession, name="del_profession"),
    path('professions/new_employee/', views.new_profession, name="new_profession"),


]