from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    #apps
    (r'^', include('app.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^gallery/', include('gallery.urls')),


    #comments
    (r'^comments/', include('django.contrib.comments.urls')),

    #admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    #static media
    #WARNING: dev only
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),

)
