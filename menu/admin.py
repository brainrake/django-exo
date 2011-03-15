from django.contrib import admin
from django.http import HttpResponseRedirect
from models import *

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(SubmenuItem)
