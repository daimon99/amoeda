# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import viewsets, decorators
from rest_framework.request import Request
from rest_framework.response import Response
from django.utils.timezone import now

from amoeba.biz import core
from .. import models as m


def validate(json_input: dict):
    """校验输入有效性"""
    pass


class BatchApi(viewsets.ReadOnlyModelViewSet):
    queryset = m.Batch.objects.all()

    @decorators.action(['POST'])
    def record(self, request: Request):
        """

        :param request: json格式::

            {
                company_id: '',
                batch_name: '',
                batch_memo: '',
                journals: {[{
                    coa_id: '',
                    department_id: '',
                    project_id: '',
                    product_id: '',
                    amount: '',
                    memo: ''
                }]}
            }
        :return:
        """
        json_input = request.data
        try:
            validate(json_input)
        except ValueError as e:
            return Response(data={'code': -1, 'msg': str(e)})

        user: User = request.user
        company_id = json_input['company_id'] or user.userext.company_id
        batch_name = json_input['batch_name'] or m.Batch.default_batch_name()
        batch_memo = json_input['batch_memo']
        batch = m.Batch(company_id=company_id, batch_name=batch_name, batch_memo=batch_memo)
        journals = json_input['journals']
        journal_objs = list()
        for j in journals:
            journal_objs.append(m.Journal(
                batch=batch,
                coa_id=j['coa_id'],
                department_id=j['department_id'],
                project_id=j['project_id'],
                product_id=j['product_id'],
                amount=j['amount'],
                memo=j['memo']
            ))
        core.record(user, batch, journal_objs)
        return Response({'code': 0, 'msg': '日记账保存成功'})
