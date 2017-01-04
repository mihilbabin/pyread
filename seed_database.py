import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyread.settings')

import django
django.setup()

from pages.models import Category, Page


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
        "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/"}
    ]
    django_pages = [
        {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/"}
    ]
    other_pages = [
        {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
        "url":"http://flask.pocoo.org"}
    ]
    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages} }

    for category, category_data in cats.items():
        c = add_category(category)
        print(c)
        for page in category_data['pages']:
            add_page(c, page['title'], page['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('- {} - {}'.format(c, p))

def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

if __name__ == '__main__':
    print("Starting population script")
    populate()
