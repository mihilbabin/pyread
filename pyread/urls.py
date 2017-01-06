from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pages import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^read/', include('pages.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^$', views.index, name='root'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
