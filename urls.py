from django.conf.urls.defaults import *
from Guardabosques.views import hello, current_date, hours_ahead
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    ('^hello/$',hello),
    ('^time/$',current_date),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
     'django.views.static.serve', {'document_root' : settings.STATIC_ROOT })
    # Examples:
    # url(r'^$', 'pepe.views.home', name='home'),
    # url(r'^pepe/', include('pepe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
