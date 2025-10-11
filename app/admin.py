from django.contrib import admin
from django.db import models
from .models import UserAdmin, UserAnggota, Article, Category, Page
from import_export.admin import ImportExportModelAdmin
from .admin_resources import UserAnggotaResource


class UserAnggotaImport(ImportExportModelAdmin):
    resource_class = UserAnggotaResource  # Import User DOSEN

admin.site.register(UserAnggota, UserAnggotaImport)
admin.site.register(UserAdmin)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Page)
