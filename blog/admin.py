from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms
from models import *


class ArticleAdmin(admin.ModelAdmin):
    '''Admin for Blog Article'''
    def sites(object):
        '''return a string listing site names for an object'''
        return ', '.join([s.name for s in object.sites.all()])

    def save_model(self, request, obj, form, change):
        if not change: #save creating user
            obj.user = request.user
        obj.save()

    list_display = ('title','date_published','user',sites)
    list_display_links = ('title',)
    list_filter = ('sites','user',)
    search_fields = ('title','content')
    date_hierarchy = 'date_published'
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('user','date_created','date_modified')
    fieldsets = (
        (None, {
            'fields': ( ('title','slug'), 'content')
        }),
        (_('Publishing options'), {
            'fields': ('user',('date_published','date_created','date_modified'),'enable_comments','sites')
        }),
    )

admin.site.register(Article, ArticleAdmin)
