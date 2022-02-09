import csv
from django.contrib import admin
from .models import *
# Register your models here.
from django.http import HttpResponse
from .forms import forms


# admin.site.register(User)



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected csv"


@admin.register(User)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("firstname", "lastname", "companyname", "consultant", "email")
    actions = ["export_as_csv"]

"""


class SomeModelAdmin(admin.ModelAdmin):

    def admin_action(self, request, queryset):


        actions = ["export_as_csv"]






class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={User}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


#@admin.register(User)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("Vorname", "Nachname", "Firma", "Email")
    actions = ["export_as_csv"]




"""
