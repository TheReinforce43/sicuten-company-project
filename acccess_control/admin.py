from django.contrib import admin

# Register your models here.

from acccess_control.Model.accces_log_model import AccessLog


admin.site.register(AccessLog)
