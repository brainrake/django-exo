from django.db import models
from django.utils.translation import ugettext_lazy as _

class Menu(models.Model):
    title = models.CharField(_('title'), max_length=200)

    def __unicode__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, verbose_name=_('menu'))
    title = models.CharField(_('title'), max_length=200)
    url = models.CharField(max_length=1000)
    ordering = models.IntegerField(_('ordering'),default=0)

    class Meta:
        ordering=('ordering',)

    def __unicode__(self):
        return self.title


class SubmenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name=_('menu item'))
    title = models.CharField(_('title'), max_length=200)
    url = models.CharField(max_length=1000)
    ordering = models.IntegerField(_('ordering'),default=0)

    class Meta:
        ordering=('ordering',)

    def __unicode__(self):
        return self.title
