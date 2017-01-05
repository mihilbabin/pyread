from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('pages/categories.html')
def category_list(active=None):
    return {'categories': Category.objects.all(), 'active_cat': active}
