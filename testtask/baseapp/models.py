from django.db import models


class ProfessionsManager(models.Manager):
    def create_profession(self, tittle):
        profession = self.create(tittle=tittle)
        return profession
class Professions(models.Model):
    tittle = models.CharField(max_length=20, unique=True, default='без должности')
    objects = ProfessionsManager()

    class Meta:
        db_table = 'professions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f"{self.tittle}"

class Employees(models.Model):
    firstname = models.CharField(max_length=20, blank=False)
    midname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=False)
    profession = models.ForeignKey(Professions, default="без должности", on_delete=models.SET_DEFAULT, related_name='professions', to_field='tittle')
    date_hired = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'employees'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['-date_hired']
        #indexes = models.Index(fields=['-date_hired'])

    def __str__(self):
        if self.midname is None:
            return f"{self.lastname[:50]} {self.firstname[:1]}."

        return f"{self.lastname[:50]} {self.firstname[:1]}.{self.midname[:1]}."



# Create your models here.
