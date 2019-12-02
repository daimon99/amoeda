from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render

from . import models as m

admin.site.site_header = 'Amoeba - 阿米巴经营'
admin.site.site_title = 'Amoeba'
admin.site.index_title = '首页'
admin.site.site_url = None


# Register your models here.

@admin.register(m.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.Coa)
class CoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', )
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )
    ordering = ('code', )


@admin.register(m.Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )


@admin.register(m.UserExt)
class UserExtAdmin(admin.ModelAdmin):
    list_display = ('id',)
    # list_select_related = ('task', )
    # autocomplete_fields = ('project', 'task')
    # search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    # actions = ('', )
