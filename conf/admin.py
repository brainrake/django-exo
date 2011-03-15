from django.contrib import admin
from django.http import HttpResponseRedirect
from models import *

class ConfAdmin(admin.ModelAdmin):
    pass


admin.site.register(Conf, ConfAdmin)
