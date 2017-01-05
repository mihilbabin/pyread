from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<slug>[-\w]+)/$', views.category_detail, name='detail'),
    url(r'^category/new/$', views.category_create, name='create'),
    url(r'^(?P<slug>[-\w]+)/page/new/$', views.page_create, name='page_create')
]
