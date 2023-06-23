from django import template
from ..models import ProfileModel

register = template.Library()


@register.simple_tag
def get_profile():
    return ProfileModel.objects.all()
