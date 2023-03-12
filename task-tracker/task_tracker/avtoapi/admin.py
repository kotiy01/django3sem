from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class executorsAdmin (ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'executor_name', 'post_name','phone')
    list_display_links = ('id','executor_name', 'phone')
    search_fields = ('executor_name', 'phone')


@admin.register(Posts)
class postsAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'post_name')
    list_display_links = ('id', 'post_name')

    class Meta:
        proxy = True


@admin.register(Statuses)
class statusesAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    class Meta:
        proxy = True


@admin.register(Projects)
class projectsAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'project_name')
    list_display_links = ('id', 'project_name')

    class Meta:
        proxy = True


@admin.register(Tasks)
class tasksAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'TaskDesc', 'DateStart','DateEnd','ProjectName', 'ExecutorName','StatusName')
    list_display_links = ('id', 'TaskDesc', 'DateStart','DateEnd','ProjectName', 'ExecutorName','StatusName')

    class Meta:
        proxy = True

admin.site.register(Executors, executorsAdmin)

