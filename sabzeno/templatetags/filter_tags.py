from django import template

register = template.Library()


#جدا کردن عداد سه رقم سه رقم
@register.filter
def intcomma_custom(value):
    try:
        return "{:,}".format(int(value))
    except (ValueError, TypeError):
        return value