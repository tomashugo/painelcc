from django import template

register = template.Library()

@register.filter(name='to_exclamation')
def to_exclamation(value):
   return value.replace("&","!")
