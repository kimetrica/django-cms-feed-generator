from django.conf.urls import *
from feed_generator.feeds import RSSFeed
from django.conf.urls import include, url

# urlpatterns = patterns('',
#     (r'^rss/$', RSSFeed()),
# )
# urlpatterns += patterns('feed_generator.views',
#     (r'^get_file/', 'get_file'),
# )

urlpatterns = [
  url(r'^rss/$', RSSFeed(), name='RSSFeed'),
]
