from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter('reportkey')    
def reportkey(dict_data, key):
    if key in dict_data:
        return dict_data.get(key)