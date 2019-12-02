# coding: utf-8
from typing import List, Tuple
from django.db.transaction import atomic
from ..models import Journal, JournalHead
from django.utils.timezone import now


@atomic
def record(user, head: JournalHead, journals: List[Journal]):
    """
    记账

    :param user:
    :param head:
    :param journals: 无须给batch 账值。这里会赋值
    :return:
    """
    head.save()
    for j in journals:
        j.head = head
    Journal.objects.bulk_create(journals)
