# Generated by Django 4.2.7 on 2023-11-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0007_alter_employees_profession_alter_professions_tittle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professions',
            name='tittle',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
