from django import template

register = template.Library()


@register.filter(is_safe=True)
def div(value, div):
    return round((value / div) * 100, 2)
