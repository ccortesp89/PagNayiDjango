from django.contrib import admin
from .models import entrevista
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class EntrevistaResource(resources.ModelResource):
    class Meta:
        model = entrevista

class EntrevistaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['artista']
    search_fields = ['artista']
    list_per_page = 10
    resource_class = EntrevistaResource

admin.site.register(entrevista, EntrevistaAdmin)