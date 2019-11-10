from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from sang.models import Sang


@admin.register(Sang)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )