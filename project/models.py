from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedUUIDModel

class Project(TimeStampedUUIDModel):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name=_("slug"), always_update=True)
    description = models.CharField(max_length=255, verbose_name=_('description'))
    body = models.TextField(verbose_name=_('body'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('image'), blank=True, null=True, upload_to='images/', default='images/default.png')
    source_link = models.CharField(max_length=128, verbose_name=_('source code'), blank=True, null=True)
    demo_link = models.CharField(max_length=128, verbose_name=_('demo link'), blank=True, null=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ('-created_at', '-updated_at')

    def __str__(self):
        return self.title

class Tag(TimeStampedUUIDModel):
    name = models.CharField(max_length=128, verbose_name=_('name'))

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        ordering = ('-created_at', '-updated_at')
    
    def __str__(self):
        return self.name
    