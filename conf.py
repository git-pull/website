# -*- coding: utf-8 -*-

import alabaster

extensions = [
  'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
  'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alabaster'
]

html_title = 'Tony\'s Confucian Gentlemen Club'

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'confucian gentleman\'s club 🍵'
copyright = u'2013 - 2017, Tony Narlock'  # NOQA

version = '0.0'
release = '0.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme_path = [alabaster.get_path()]
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'img/tony.svg',
}
html_sidebars = {
    '**': [
        'about.html',
        'star.html',
        # 'navigation.html',
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
    'tmuxp': ('https://tmuxp.readthedocs.org/en/latest/', None),
    'libtmux': ('https://libtmux.readthedocs.io/en/latest/', None),
    'libvcs': ('https://libvcs.readthedocs.org/en/latest/', None),
    'vcspull': ('https://vcspull.readthedocs.org/en/latest/', None),
    'dockerjournal': (
      'http://docker-recipes.readthedocs.org/en/latest/', None
    ),
}
