from django.contrib import admin

from . models import RawData, ColumnInfo
# Register your models here.
admin.site.register(RawData)
admin.site.register(ColumnInfo)