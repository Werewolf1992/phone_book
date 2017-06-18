from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, name):
    current_url_name = context['request'].resolver_match.url_name
    if name == current_url_name:
        return 'active'
    return ''
