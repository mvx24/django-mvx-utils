from django import template

register = template.Library()

@register.filter
def range(num):
	return xrange(num)
