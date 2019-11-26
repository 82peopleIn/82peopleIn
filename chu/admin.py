from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from chu.models import Chu


@admin.register(Chu)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

