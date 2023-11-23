from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employees)
admin.site.register(Devices)
admin.site.register(DeviceReport)
admin.site.site_header = "Admin View"
admin.site.site_title = "streamingportal"
admin.site.index_title = "Admin view"