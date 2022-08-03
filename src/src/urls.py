from django.contrib import admin
from django.urls import include, path,re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


# last line to be used to handle media during production
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
