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


@register.filter
def subtract(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return value


@register.filter
def ru_plural(value, variants):
    variants = variants.split(",")
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif 2 <= value % 10 <= 4 and \
            (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]
