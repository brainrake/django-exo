from django.conf.urls.defaults import *
from feeds import *

urlpatterns = patterns('blog.views',
    #all articles
    ('^$','articles'),

    #archive by date
    ('^(?P<year>\d\d\d\d)/$','articles'),
    ('^(?P<year>\d\d\d\d)/(?P<month>\d\d)/$','articles'),
    ('^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/$','articles'),

    #article. note lack of trailing slash.
    ('^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<slug>[\w_-]+)$','article'),

    #feeds
    (r'^rss/$', BlogFeedRss()),
    (r'^atom/$', BlogFeedAtom()),
)
