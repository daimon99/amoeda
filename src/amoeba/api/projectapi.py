# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class ProjectApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Project.objects.all()
