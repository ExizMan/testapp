from django.urls import path
from . import views

app_name = 'baseapp'
urlpatterns = [
    path('',views.index, name="index"),
    path('employees',views.employees, name='employees'),
    path('professions',views.professions,name='professions'),
    path('employees/<int:emp_id>/',views.employee, name="employee"),
    path('employees/<int:emp_id>/delete',views.del_employee, name="del_employee"),
    path('employees/new_employee/',views.new_employee, name="new_employee"),


]