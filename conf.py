# -*- coding: utf-8 -*-

import alagitpull

extensions = [
  'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
  'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alagitpull'
]

html_title = 'git-pull.com'

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'confucian gentleman\'s club 🍵'
copyright = u'2013 - 2018, Tony Narlock'  # NOQA

version = '0.0'
release = '0.0'

exclude_patterns = ['_build', '.venv']

pygments_style = 'sphinx'

html_theme_path = [alagitpull.get_path()]
html_theme = 'alagitpull'
html_favicon = 'favicon.ico'
html_theme_options = {
    'logo': 'img/bagua.png',
    'projects': alagitpull.projects,
}
html_sidebars = {
    '**': [
        'about.html',
        'relations.html',
        'more.html',
    ]
}

html_static_path = ['_static']

htmlhelp_basename = 'confuciangentlemansclubdoc'


latex_elements = {
}

latex_documents = [
  ('index', 'confuciangentlemansclub.tex', u'confucian gentleman\'s',
   u'Tony Narlock', 'manual'),
]

man_pages = [
    ('index', 'confuciangentlemansclub', u'confucian gentleman\'s club',
     [u'Tony Narlock'], 1)
]

texinfo_documents = [
  ('index', 'confuciangentlemansclub', u'confucian gentleman\'s club',
   u'Tony Narlock', 'confuciangentlemansclub', 'Scribe.',
   'Miscellaneous'),
]

intersphinx_mapping = {
    'https://docs.python.org/2/': None,
    'sphinx': ('https://sphinx.readthedocs.io/en/latest/', None),
    'tmuxp': ('https://tmuxp.git-pull.com/en/latest/', None),
    'libtmux': ('https://libtmux.git-pull.com/en/latest/', None),
    'libvcs': ('https://libvcs.git-pull.com/en/latest/', None),
    'vcspull': ('https://vcspull.git-pull.com/en/latest/', None),
    'cihai': ('https://cihai.git-pull.com/en/latest/', None),
    'cihai-cli': ('https://cihai-cli.git-pull.com/en/latest/', None),
    'unihan-etl': ('https://unihan-etl.git-pull.com/en/latest/', None),
    'django': (
        'https://docs.djangoproject.com/en/1.11/',
        'https://docs.djangoproject.com/en/1.11/_objects/'
    ),
    'flask': ('http://flask.pocoo.org/docs/', None),
    'flask-sqlalchemy': ('http://flask-sqlalchemy.pocoo.org/2.2/', None),
    'werkzeug': ('http://werkzeug.pocoo.org/docs/0.12/', None),
    'jinja': ('http://jinja.pocoo.org/docs/dev', None),
    'sqlalchemy': ('http://docs.sqlalchemy.org/en/latest/', None),
    'uwsgi': ('https://uwsgi-docs.readthedocs.io/en/latest/', None),
}
