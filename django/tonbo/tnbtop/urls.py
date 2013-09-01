from django.conf.urls import patterns, include, url

urlpatterns = patterns('tnbtop.views',
    url(r'^$', 'index'),
    url(r'^create$', 'create'),
    url(r'^(?P<board_id>\d+)/$', 'display', name="board-display"),
    url(r'^(?P<board_id>\d+)/put/$', 'put'),
)
