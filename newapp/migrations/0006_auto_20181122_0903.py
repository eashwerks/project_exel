# Generated by Django 2.1.3 on 2018-11-22 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_employee_average_in_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrences', to='newapp.Employee'),
        ),
    ]
