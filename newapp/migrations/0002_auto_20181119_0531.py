# Generated by Django 2.1.3 on 2018-11-19 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagetime',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]