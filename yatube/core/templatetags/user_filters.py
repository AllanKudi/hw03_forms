from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def text_cut(text):
    text_cut = ''
    for i in range(len(text)):
        text_cut += text[i]
        if i == 30:
            return text_cut
