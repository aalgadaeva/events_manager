from django import template
from ..models import Event

register = template.Library()


@register.simple_tag(name='total')
def total_attending():
    pass
