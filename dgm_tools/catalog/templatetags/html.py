from django import template
from bs4 import BeautifulSoup


register = template.Library()


@register.filter
def clean_extra_style(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all():
        del tag['style']
        del tag['class']

    return soup.prettify()
