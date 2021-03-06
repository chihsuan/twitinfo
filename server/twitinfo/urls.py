from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('twitinfo.views',
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DOC_ROOT}),
     (r'^$', 'twitinfo'),
    (r'^results', 'search_results'),
    (r'^create_event/detail/(?P<event_id>\d+)/$', 'event_details'),
    (r'^create_event/$', 'create_event'),
    (r'^detail/create_graph/(?P<event_id>\d+)/$', 'create_graph'),
    (r'^detail/create_piChart/(?P<event_id>\d+)/$', 'create_pieChart'),
    (r'^detail/create_map/(?P<event_id>\d+)/$', 'create_map'),
    (r'^display_tweets/(?P<event_id>\d+)/$', 'display_tweets'), 
    (r'^display_links/(?P<event_id>\d+)/$', 'display_links'),
    (r'^twitinfo', include('twitinfo.url.urls')),
)
