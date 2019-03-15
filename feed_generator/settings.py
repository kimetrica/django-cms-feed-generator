from django.conf import settings

feed_limit = getattr(settings, 'FEEDGENERATOR_FEED_LIMIT', 20)
exclude_keyword = getattr(settings, 'FEEDGENERATOR_EXCLUDE_KEYWORD', 'No Search')

