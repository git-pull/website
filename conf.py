# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join

import alagitpull

sys.path.append(abspath(join(dirname(__file__), "_ext")))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "alagitpull",
    'myst_parser',
]

myst_enable_extensions = ["colon_fence"]

html_title = "git-pull.com"

templates_path = ["_templates"]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}

master_doc = "index"

project = u"confucian gentleman's club 🍵"
copyright = u"2013 - , Tony Narlock"  # NOQA

version = "0.0"
release = "0.0"

exclude_patterns = ["_build", ".venv"]

pygments_style = "sphinx"

alagitpull_internal_hosts = [
    "git-pull.com",
    "www.git-pull.com",
    "0.0.0.0",
]
alagitpull_external_hosts_new_window = True

html_theme_path = [alagitpull.get_path()]
html_theme = "alagitpull"
html_favicon = "_static/favicon.ico"
html_scaled_image_link = False  # don't add link to scaled images
html_theme_options = {
    "logo": "img/bagua.png",
    'projects': alagitpull.projects,
    'project_name': 'git-pull // Tony Narlock',
    'project_title': 'git-pull // Tony Narlock',
    'project_description': (
        'Homepage of Tony Narlock, open source programmer and author'
    ),
    'project_url': 'https://www.git-pull.com',
    'show_meta_manifest_tag': True,
    'show_meta_og_tags': True,
    'show_meta_app_icon_tags': True,
}
html_sidebars = {"**": ["about.html", "relations.html", "more.html"]}

html_static_path = ["_static"]
html_extra_path = ["manifest.json"]

htmlhelp_basename = "confuciangentlemansclubdoc"


latex_elements = {}

latex_documents = [
    (
        "index",
        "confuciangentlemansclub.tex",
        u"confucian gentleman's",
        u"Tony Narlock",
        "manual",
    ),
]

man_pages = [
    (
        "index",
        "confuciangentlemansclub",
        u"confucian gentleman's club",
        [u"Tony Narlock"],
        1,
    )
]

texinfo_documents = [
    (
        "index",
        "confuciangentlemansclub",
        u"confucian gentleman's club",
        u"Tony Narlock",
        "confuciangentlemansclub",
        "Scribe.",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {
    "https://docs.python.org/2/": None,
    "tmuxp": ("https://tmuxp.git-pull.com/en/latest/", None),
    "libtmux": ("https://libtmux.git-pull.com/en/latest/", None),
    "libvcs": ("https://libvcs.git-pull.com/", None),
    "vcspull": ("https://vcspull.git-pull.com/en/latest/", None),
    "cihai": ("https://cihai.git-pull.com/en/latest/", None),
    "cihai-cli": ("https://cihai-cli.git-pull.com/en/latest/", None),
    "unihan-etl": ("https://unihan-etl.git-pull.com/en/latest/", None),
    "django-slugify-processor": (
        "https://django-slugify-processor.git-pull.com/en/latest/",
        None,
    ),
    "django": (
        "https://docs.djangoproject.com/en/1.11/",
        "https://docs.djangoproject.com/en/1.11/_objects/",
    ),
}
