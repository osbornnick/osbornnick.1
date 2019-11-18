from django import template

register = template.Library()


@register.filter()
def mod(num, max):
    return (num % max) + 1
