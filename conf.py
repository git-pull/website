# -*- coding: utf-8 -*-

import alagitpull

extensions = [
  'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
  'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alagitpull'
]

html_title = 'Tony\'s Confucian Gentlemen Club'

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'confucian gentleman\'s club 🍵'
copyright = u'2013 - 2017, Tony Narlock'  # NOQA

version = '0.0'
release = '0.0'

exclude_patterns = ['_build', '.venv']

pygments_style = 'sphinx'

html_theme_path = [alagitpull.get_path()]
html_theme = 'alagitpull'
html_theme_options = {
    'logo': 'img/tony.svg',
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
    'http://docs.python.org/': None,
    'pip': ('http://sphinx.readthedocs.org/en/latest/', None),
    'tmuxp': ('https://tmuxp.git-pull.com/en/latest/', None),
    'libtmux': ('https://libtmux.git-pull.com/en/latest/', None),
    'libvcs': ('https://libvcs.git-pull.com/en/latest/', None),
    'vcspull': ('https://vcspull.git-pull.com/en/latest/', None),
    'cihai': ('https://cihai.git-pull.com/en/latest/', None),
    'cihai-cli': ('https://cihai-cli.git-pull.com/en/latest/', None),
    'unihan-etl': ('https://unihan-etl.git-pull.com/en/latest/', None),
    'dockerjournal': (
      'http://docker-recipes.readthedocs.org/en/latest/', None
    ),
    'django': (
        'http://docs.djangoproject.com/en/1.11/',
        'http://docs.djangoproject.com/en/1.11/_objects/'
    ),
    'flask': ('http://flask.pocoo.org/docs/', None),
    'flask-sqlalchemy': ('http://flask-sqlalchemy.pocoo.org/2.2/', None),
    'werkzeug': ('http://werkzeug.pocoo.org/docs/', None),
    'jinja': ('http://jinja2.pocoo.org/docs/dev', None),
    'sqlalchemy': ('http://docs.sqlalchemy.org/en/latest/', None)
}
