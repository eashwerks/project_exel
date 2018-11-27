from time import strptime
from django.shortcuts import render, redirect
import pandas as pd
from django.urls import reverse
from django.views.generic import TemplateView
from rest_auth.views import LogoutView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, authentication, status

from .serializers import EmployeeSerializer
from .models import Occurrence, Employee


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = (authentication.TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        if request.GET:
            name_str = request.GET.get('e_name', None)
            start_date = request.GET.get('start_date', None)
            end_date = request.GET.get('end_date', None)

            queryset = self.queryset.filter(name=name_str, occurrences__in_time__range=(
                start_date, end_date)) if name_str and start_date else self.queryset.filter(
                name=name_str) if not start_date and not end_date else self.queryset.filter(
                occurrences__in_time__range=(start_date, end_date))

            serializer = self.get_serializer(queryset, many=True)
            data = ([i for n, i in enumerate(serializer.data) if i not in serializer.data[n + 1:]])

        else:
            serializer = self.get_serializer(self.queryset, many=True)
            data = serializer.data
        return Response(data)


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class FileUploadView(APIView):
    # parser_classes = (FormParser, MultiPartParser)
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request, filename='tinto.xls', formate=None):
        my_file = request.data['file']
        excel_file = pd.read_excel(my_file)
        excel_file.columns = excel_file.loc['Days']
        avg_in_time = excel_file.loc['InTime'].iterrows()
        emp = excel_file.loc['Employee:'].iterrows()

        a = str(strptime(excel_file.iloc[0].dropna().tolist()[1][:3], '%b').tm_mon)

        for (l, j), (m, i) in zip(avg_in_time, emp):

            keys = (dict(j.dropna()).keys())
            values = (dict(j.dropna()).values())

            emp_obj = Employee.objects.create(id=int(((i[2].split(':'))[0]).strip(' ')),
                                              name=((str(i[2]).split(':'))[1]).strip(' '))
            for h, o in zip(keys, values):
                date_at = '2018-' + a + '-' + h[:1]
                occu = date_at + " " + o

                Occurrence.objects.create(employee=emp_obj, in_time=occu)
        return Response(my_file.name, status.HTTP_201_CREATED)
