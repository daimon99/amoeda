# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class DepartmentApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Department.objects.all()
