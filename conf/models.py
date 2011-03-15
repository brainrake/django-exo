from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

class Conf(models.Model):
    site = models.OneToOneField(Site, verbose_name=_("site"))

    #define your configuration fields here


    class Meta:
        verbose_name = _('site configuration')
        verbose_name_plural = _('site configurations')

    #TODO: i18n
    def __unicode__(self):
        return "Configuration for %s" % unicode(self.site)

