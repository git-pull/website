# -*- coding: utf-8 -*-
import sys
from os.path import join, dirname, abspath

import alagitpull

sys.path.append(abspath(join(dirname(__file__), "_ext")))

extensions = [
  'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
  'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alagitpull', 'external',
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
    'tmuxp': ('https://tmuxp.git-pull.com/en/latest/', None),
    'libtmux': ('https://libtmux.git-pull.com/en/latest/', None),
    'libvcs': ('https://libvcs.git-pull.com/en/latest/', None),
    'vcspull': ('https://vcspull.git-pull.com/en/latest/', None),
    'cihai': ('https://cihai.git-pull.com/en/latest/', None),
    'cihai-cli': ('https://cihai-cli.git-pull.com/en/latest/', None),
    'unihan-etl': ('https://unihan-etl.git-pull.com/en/latest/', None),
    'django-slugify-processor': (
        'https://django-slugify-processor.git-pull.com/en/latest/', None,
    ),
    'django': (
        'https://docs.djangoproject.com/en/1.11/',
        'https://docs.djangoproject.com/en/1.11/_objects/'
    ),
}
