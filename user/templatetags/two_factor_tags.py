from django import template

from two_factor.plugins.registry import registry

register = template.Library()


@register.filter
def as_action(device):
    method = registry.method_from_device(device)
    return method.get_action(device)


@register.filter
def as_verbose_action(device):
    method = registry.method_from_device(device)
    return method.get_verbose_action(device)


@register.filter(name="add_classes")
def add_classes(value, args):
    classes = value.field.widget.attrs.get("class", "")

    if classes:
        classes = classes.slipt(" ")
    else:
        classes = []

    new_classes = args.split(" ")
    for c in new_classes:
        if c not in classes:
            classes.append(c)
    return value.as_widget(attrs={"class": "".join(classes)})
