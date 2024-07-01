from django import template
from django.db.models import Model

register = template.Library()

@register.simple_tag()
def get_model_class(model: Model):
    return f"{model.__module__}.{model.__class__.__name__}"
