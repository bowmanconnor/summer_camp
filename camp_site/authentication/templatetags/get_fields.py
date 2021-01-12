from django import template

register = template.Library()

@register.filter
def get_fields(obj):
    if obj:
        return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]
    
@register.filter
def num_campers(obj, camp):
    num = 0
    if obj:
        for x in obj.filter(camp=camp):
            num += 1
        return num