# coding: utf-8

from rest_framework import viewsets
from .. import models as m


class ProductApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Product.objects.all()
