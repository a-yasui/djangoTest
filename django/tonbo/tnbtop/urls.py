from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'display'),
    url(r'^(?P<poll_id>\d+)/put/$', 'put'),
)
