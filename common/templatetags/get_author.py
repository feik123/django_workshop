from django import template

from FurryFunnies.utils import get_user_obj


register = template.Library()

@register.simple_tag(name='get_author')
def get_author():
    return get_user_obj()