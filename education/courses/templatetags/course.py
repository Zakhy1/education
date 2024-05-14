from django import template

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter
def add_class(field, css_class: str):
    return field.as_widget(attrs={'class': css_class})


@register.filter
def add_rows(field, rows: int):
    return field.as_widget(attrs={'rows': rows, 'class': 'form-control', 'style': 'width: 100%'})


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name
