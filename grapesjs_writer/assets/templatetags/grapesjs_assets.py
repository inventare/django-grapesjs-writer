import json
from django import template
from django.http import HttpRequest
from django.db.models import Model
from django.utils.safestring import mark_safe
from grapesjs_writer.templatetags.grapesjs import get_model_class
from grapesjs_writer.assets.models import AssetItem

register = template.Library()

def _get_asset_dict(asset: AssetItem, request: HttpRequest):
    src = request.build_absolute_uri(asset.image.url)
    return src
    return { 'type': 'image', 'src': src, 'name': asset.display_name }

@register.simple_tag()
def get_assets(model: Model, request: HttpRequest):
    model_class = get_model_class(model)
    instances = AssetItem.objects.filter(template_model_class=model_class).all()
    data = list(map(lambda item: _get_asset_dict(item, request), instances))
    return mark_safe(json.dumps(data))
