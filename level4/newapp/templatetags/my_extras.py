from django import template
register = template.Library()

@register.filter(name='cut')
def cut(value, args):
    print(value)
    print(args)
    return value.replace(args,'')

