# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class JournalApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Journal.objects.all()
