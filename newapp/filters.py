from django_filters import rest_framework as filters

from newapp.models import Employee, Occurrence


class EmployeeFilter(filters.FilterSet):
    max_date = filters.DateFromToRangeFilter(field_name='occurrences__in_time')

    class Meta:
        model = Employee
        fields = ['name', 'max_date']


class OccurrenceFilter(filters.FilterSet):
    max_date = filters.DateFromToRangeFilter(field_name='in_time')

    class Meta:
        model = Occurrence
        fields = ['employee__name', 'max_date']
