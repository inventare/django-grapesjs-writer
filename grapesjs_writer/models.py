from django.db import models
from django.utils.translation import gettext_lazy as _

class TemplateBase(models.Model):
    name = models.CharField(
        _('template name'),
        max_length=150,
        unique=True
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    template_code = models.TextField(_('template code'), blank=True, default='')
    template_data = models.JSONField(_('template data'), default=dict)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = _('template')
        verbose_name_plural = _('templates')
