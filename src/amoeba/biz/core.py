# coding: utf-8
from typing import List, Tuple
from django.db.transaction import atomic
from ..models import Journal, Batch
from django.utils.timezone import now


@atomic
def record(user, batch: Batch, journals: List[Journal]):
    """
    记账

    :param user:
    :param batch:
    :param journals: 无须给batch 账值。这里会赋值
    :return:
    """
    batch.save()
    for j in journals:
        j.batch = batch
    Journal.objects.bulk_create(journals)
