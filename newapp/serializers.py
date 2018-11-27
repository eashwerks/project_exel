from abc import ABC
import numpy as np
from datetime import datetime
from rest_framework import serializers

from .models import Employee, Occurrence


class FilteredListSerializer(serializers.ListSerializer, ABC):

    def to_representation(self, data):
        if 'start_date' in self.context['request'].query_params:
            data = data.filter(in_time__range=(self.context['request'].query_params['start_date'],
                                               self.context['request'].query_params['end_date']))
        else:
            pass
        return super(FilteredListSerializer, self).to_representation(data)


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Occurrence
        fields = ('in_time',)


class EmployeeSerializer(serializers.ModelSerializer):
    occurrences = OccurrenceSerializer(many=True, read_only=True)
    average_in_time = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('name', 'id', 'average_in_time', 'occurrences')

    def get_average_in_time(self, obj):
        if 'start_date' in self.context['request'].query_params:
            lst = list(obj.occurrences.filter(in_time__range=(self.context['request'].query_params['start_date'],
                                                              self.context['request'].query_params['end_date'])))
        else:
            lst = list(obj.occurrences.all())
        dates = list(
            map(lambda w: datetime.strptime(str(w).split(' - ')[1][:8], '%H:%M:%S'), lst))
        mean = None

        if len(dates):
            mean = str(np.array(dates, dtype='datetime64[s]').view('i8')
                       .mean()
                       .astype('datetime64[s]'))[11:]

        return mean
