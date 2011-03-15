from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class GalleryOnlineManager(models.Manager):
    '''Manager for galleries on the current site'''
    def get_query_set(self):
        return super(GalleryOnlineManager,self).get_query_set().filter(
            sites=Site.objects.get_current()
        )

class Gallery(models.Model):
    '''Image Gallery'''
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200)

    user = models.ForeignKey(User, verbose_name = _('user'))
    sites = models.ManyToManyField(Site,verbose_name=_('sites'),default=[Site.objects.get_current().id], blank=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    objects = models.Manager()
    online = GalleryOnlineManager()

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Image(models.Model):
    '''Image'''
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'))
    title = models.CharField(_('title'), max_length=200, blank=True)
    image = models.ImageField(_('image'), upload_to='uploads/gallery/')
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.image.path.rpartition('/')[2]
        return super(Image, self).save(*args, **kwargs)

