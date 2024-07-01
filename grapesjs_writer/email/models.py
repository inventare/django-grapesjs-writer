from django.db import models
from django.utils.translation import gettext_lazy as _
from grapesjs_writer.models import TemplateBase

class EmailTemplateManager(models.Manager):
    def get_by_template_id(self, id: str):
        return self.get(template_id=id)

class EmailTemplate(TemplateBase):
    template_id = models.CharField(_('template id'), max_length=150)

    objects: EmailTemplateManager = EmailTemplateManager()

    class Meta:
        verbose_name = _('email template')
        verbose_name_plural = _('email templates')
