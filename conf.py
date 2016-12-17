# -*- coding: utf-8 -*-
#
import sys, os

extensions = [
  'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
  'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alabaster'
]

html_title = 'Tony Narlock\'s Confucian Gentlemen Club'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'confucian gentleman\'s club'
copyright = u'2013 - 2016, Tony Narlock'  # NOQA

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'
# The full version, including alpha/beta/rc tags.
release = '0.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

import alabaster

html_theme_path = [alabaster.get_path()]
html_theme = 'alabaster'
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
    'libtmux': ('https://libtmux.readthedocs.io/', None),
    'libvcs': ('https://libvcs.readthedocs.org/en/latest/', None),
    'vcspull': ('https://vcspull.readthedocs.org/en/latest/', None),
    'dockerjournal': ('http://docker-recipes.readthedocs.org/en/latest/', None),
}
