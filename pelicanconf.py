AUTHOR = 'pandavas89'
SITENAME = 'PlayEng Ground'
SITEURL = 'https://blog.tykl.me'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'KR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'ss_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Contents',
        },
    },
    'output_format': 'html5',
}

# Social widget
SOCIAL = (
    ('Instagram', 'https://www.instagram.com/pandavas89/'),
)

DEFAULT_PAGINATION = 10

DEFAULT_DATE_FORMAT = '%Y/%m/%d'

#THEME = 'theme/aboutwilson'
THEME = 'theme/bootstrap_notion'

USE_FOLDER_AS_CATEGORY = True

DISQUS_SITENAME = 'pandavas'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True