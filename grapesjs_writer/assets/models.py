import os
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to_path(instance, filename):
    cls = str(instance.template_model_class).replace(".", '_')
    return f"gapesjs/assets/{cls}/{filename}"

class AssetItem(models.Model):
    template_model_class = models.TextField(_('template model class'))
    image = models.ImageField(_('image'), upload_to=upload_to_path)
    display_name = models.CharField(_('display name'), max_length=150, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.display_name and self.image is not None:
            name = os.path.basename(self.image.path)
            if len(name) > 150:
                name = name[0, 147] + '...'
            self.display_name = name
        super(AssetItem, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.display_name
    
    class Meta:
        verbose_name = _('Asset item')
        verbose_name_plural = _('Assets itens')
