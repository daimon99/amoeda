# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class CompanyApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Company.objects.all()
