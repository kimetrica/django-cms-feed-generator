from cms.models import Page
from django.db import models
from fields import ImageField

class PageRSSFeed(models.Model):
    page = models.OneToOneField(Page)
    short_description = models.CharField(max_length=255, blank=True, null=False)
    image_url = ImageField(max_length=2000, blank=True, null=False)
    not_visible_in_feed = models.BooleanField(verbose_name='Exclude from RSS feed')

    class Meta:
        verbose_name = 'RSS'
        verbose_name_plural = 'RSS'

    def __unicode__(self):
        return self.short_description[0:50]
