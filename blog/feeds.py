from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from models import Article

#TODO:i18n
class BlogFeedRss(Feed):
    title = "Latest Articles on %s" % Site.objects.get_current()
    link = '/'
    description = "Latest Articles on %s" % Site.objects.get_current()

    def items(self):
        return Article.online.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

class BlogFeedAtom(BlogFeedRss):
    feed_type = Atom1Feed
    subtitle = BlogFeedRss.description
