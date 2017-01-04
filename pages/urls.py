from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<slug>[-\w]+)$', views.category_detail, name='detail')
]
