from django.urls import path
from . import views

app_name = 'baseapp'
urlpatterns = [
    path('employees',views.employees, name='employees'),
    path('professions',views.professions,name='professions'),
    path('employees/<int:emp_id>/',views.employee, name="employee"),
    path('employees/<int:emp_id>/delete')

]