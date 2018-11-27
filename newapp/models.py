

from django.db import models


class Employee(models.Model):
    id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=50, null=True)
    average_in_time = models.TimeField(null=True)

    def __str__(self):
        return '{}--{}'.format(self.id, self.name)


class Occurrence(models.Model):
    employee = models.ForeignKey(Employee, related_name='occurrences', on_delete=models.CASCADE)
    in_time = models.DateTimeField()

    def __str__(self):
        return self.in_time.strftime("%d %b,%Y - %H:%M:%S")
