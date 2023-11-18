from django.db import models



class Employees(models.Model):
    firstname = models.CharField(max_length=20, blank=False)
    midname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=False)
    profession = models.CharField(max_length=20, blank=False)
    date_hired = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'employees'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"




class Professions(models.Model):
    tittle = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'professions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


# Create your models here.
