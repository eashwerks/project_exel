# Generated by Django 2.1.3 on 2018-11-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20181121_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='average_in_time',
            field=models.TimeField(null=True),
        ),
    ]
