from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.gis import admin
admin.autodiscover()

admin.site.site_title = 'Documento Operativo per la Difesa del Suolo LR 80/2015 art.3'
admin.site.site_header = 'Documento Operativo per la Difesa del Suolo LR 80/2015 art.3'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_segnalazioni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url('', include(admin.site.urls)),
)

# media files
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT})
)

# static files
#urlpatterns += patterns('',
#     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
#)
