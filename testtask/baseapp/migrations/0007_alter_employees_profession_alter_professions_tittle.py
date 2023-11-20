# Generated by Django 4.2.7 on 2023-11-20 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_alter_employees_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profession',
            field=models.ForeignKey(default='Без должности', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='professions', to='baseapp.professions', to_field='tittle'),
        ),
        migrations.AlterField(
            model_name='professions',
            name='tittle',
            field=models.CharField(default='Без должности', max_length=20, unique=True),
        ),
    ]