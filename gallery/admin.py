from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import *

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class GalleryAdmin(admin.ModelAdmin):
    '''Admin for Gallery'''
    def sites(article):
        return ', '.join([s.name for s in article.sites.all()])

    def save_model(self, request, obj, form, change):
        if not change: #save creating user
            obj.user = request.user
        obj.save()

    list_display = ('title','date_created','user',sites)
    list_display_links = ('title',)
    list_filter = ('sites','user',)
    search_fields = ('title','image__title')
    date_hierarchy = 'date_created'
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('user','date_created')
    fieldsets = (
        (None, {
            'fields': ( ('title','slug'),)
        }),
        (_('Publishing options'), {
            'fields': ('user','date_created','sites')
        }),
    )
    inlines = [
        ImageInline
    ]



admin.site.register(Gallery, GalleryAdmin)
