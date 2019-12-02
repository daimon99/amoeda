# coding: utf-8
import coreapi
from django.db import connection
from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from urllib import parse

from django.contrib.auth.models import User
from .. import models as m
"""sample


# coding: utf-8

from rest_framework import serializers, viewsets, decorators, request, response, status
from mgcut import mgcut


class MangoDialSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=16)
    name = serializers.CharField(max_length=16)


class MangoApi(viewsets.ViewSet):
    serializers = MangoDialSerializer
    permission_classes = ()

    @decorators.action(['POST'], detail=False)
    def dial(self, req: request.Request):
        serializer = MangoDialSerializer(data=req.data)
        if serializer.is_valid():
            try:
                mgcut.go(serializer.data['mobile'], serializer.data['name'])
                return response.Response({'code': 0, 'msg': '拨叫成功'})
            except Exception as e:
                return response.Response({'code': -1, 'msg': str(e)})
        else:
            return response.Response({'code': -2, 'msg': '参数非法', 'data': serializer.errors},
                                     status=status.HTTP_400_BAD_REQUEST)


class UserExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.UserExt
        fields = ('company',)


class UserSerializer(serializers.ModelSerializer):
    userext = UserExtSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = m.User
        fields = ('id', 'username', 'userext')


class UserApi(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    schema = CustomSchema()

    @decorators.action(['GET'], detail=False)
    def current(self, request):
        user: User = request.user
        userext = request.user.userext if hasattr(request.user, 'userext') else None
        groups = [i.name for i in user.groups.all()]
        return Response({'code': 0, 'message': '调用成功', 'data': {
            'id': user.id,
            'username': user.username,
            'tel': '',
            'role': groups
        }})

    @decorators.action(['POST'], detail=False)
    def logout(self, request):
        user: User = request.user
        return Response({
            'code': 0, 'message': '登出成功'
        })
"""

