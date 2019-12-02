# coding: utf-8

from rest_framework import serializers

from .. import models as m


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.User
        fields = ('id', 'username')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Company
        fields = ('id', 'name')


class CoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Coa
        fields = ('id', 'name')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Department
        fields = ('id', 'name')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Project
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = ('id', 'name')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Journal
        fields = ('id', 'coa', 'department', 'project', 'product', 'amount', 'memo')

    coa = CoaSerializer()
    department = DepartmentSerializer()
    project = ProjectSerializer()
    product = ProductSerializer()


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Batch
        fields = ('id', 'company', 'user', 'name', 'memo', 'journals')

    journals = JournalSerializer(
        many=True,
        read_only=True,
    )


class UserExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.UserExt
        fields = ('id', 'user', 'department', 'project', 'product', 'coa_debit', 'coa_credit')

    user = UserSerializer()
    company = CompanySerializer()
    department = DepartmentSerializer()
    project = ProjectSerializer()
    product = ProductSerializer()
    coa_debit = CoaSerializer()
    coa_credit = CoaSerializer()
