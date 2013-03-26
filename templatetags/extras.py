from django.template import Library

register = Library()

def get_thumbnail(obj):
    return obj.media.thumbnail[0]

@register.simple_tag
def thumbnail_url(obj):
    return get_thumbnail(obj).url

@register.simple_tag
def thumbnail_style(obj):
    thumb = get_thumbnail(obj)
    return 'width: %spx; height: %spx;' % (thumb.width, thumb.height)