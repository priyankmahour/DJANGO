from django import template

register = template.Library()

@register.filter(name="truncate")
def truncate_n(value,n):
    result = value[0:n]
    return result

#register.filter('truncate_n',truncate_n)
