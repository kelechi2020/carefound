from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.resources import Resource

from atiku.models import ApplicantInfo, State, LocalGovernment


admin.site.site_header = 'Atiku Cares Outreach Data Management system'
admin.site.site_title = "Atiku Cares Outreach Data Management system"



@admin.register(ApplicantInfo)
class ApplicantAdmin(ImportExportModelAdmin):
    pass


@admin.register(LocalGovernment)
class ApplicantAdmin(ImportExportModelAdmin):
    pass


@admin.register(State)
class ApplicantAdmin(ImportExportModelAdmin):
    pass