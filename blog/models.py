from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
import datetime

class ArticleOnlineManager(models.Manager):
    '''Manager for online (published before now) articles that are on the current site'''
    def get_query_set(self):
        return super(ArticleOnlineManager,self).get_query_set().filter(
            date_published__lte=datetime.datetime.now(),
            sites=Site.objects.get_current()
        )


class Article(models.Model):
    '''Blog Article

    Access online articles on the current site with the 'online' manager.
    '''

    user = models.ForeignKey(User, verbose_name=_('user'))
    title = models.CharField(_('title'), max_length = 200)
    slug = models.SlugField(_('slug'), max_length=200,unique_for_date="date_published")

    content = models.TextField(_('content'), max_length = 200)

    date_published = models.DateTimeField(_('date published'))
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'),auto_now=True)

    #TODO:
    #logged_in = models.BooleanField(_('only logged in users can see this article'))
    enable_comments = models.BooleanField()
    sites = models.ManyToManyField(Site,verbose_name=_('sites'),default=[Site.objects.get_current().id], blank=True)

    objects = models.Manager()
    online = ArticleOnlineManager()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ('-date_published',)
        get_latest_by = 'date_published'
        unique_together = ('slug','date_published')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.article', [self.date_published.strftime('%Y'), self.date_published.strftime('%m'), self.date_published.strftime('%d'), self.slug])


