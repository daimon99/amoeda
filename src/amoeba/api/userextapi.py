# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class UserExtApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.UserExt.objects.all()
