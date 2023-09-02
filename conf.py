# -*- coding: utf-8 -*-
import pathlib
import sys
import typing as t
from os.path import abspath, dirname, join

if t.TYPE_CHECKING:
    from sphinx.application import Sphinx


sys.path.append(abspath(join(dirname(__file__), "_ext")))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
    "myst_parser",
]

myst_enable_extensions = [
    "colon_fence",
    "strikethrough",
    "smartquotes",
    "attrs_inline",
]

suppress_warnings = [
    # https://myst-parser.readthedocs.io/en/latest/configuration.html#build-warnings
    "myst.strikethrough",
]

html_title = "Tony Narlock"

templates_path = ["_templates"]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

master_doc = "index"

project = "confucian gentleman's club 🍵"
copyright = "1988 - , Tony Narlock"  # NOQA

version = "0.0"
release = "0.0"

exclude_patterns = ["_build", ".venv"]

pygments_style = "monokai"
pygments_dark_style = "monokai"

html_theme_path = []
html_theme = "furo"
html_favicon = "_static/favicon.ico"
html_scaled_image_link = False  # don't add link to scaled images
html_theme_options = {
    "light_logo": "img/icons/logo.svg",
    "dark_logo": "img/icons/logo-dark.svg",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/git-pull/website",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/projects.html",
        "sidebar/scroll-end.html",
    ]
}
html_static_path = ["_static"]
html_css_files = ["css/custom.css", "css/git-pull.css", "css/flexboxgrid.min.css"]
html_extra_path = ["manifest.json"]

# sphinxext.opengraph
ogp_site_url = "https://www.git-pull.com"
ogp_image = "_static/img/icons/icon-192x192.png"
ogp_description_length = "Author of software utilities built for computer programmers"
ogp_site_name = "Tony Narlock"

# sphinx-copybutton
copybutton_prompt_text = (
    r">>> |\.\.\. |> |\$ |\# | In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
)
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True

# sphinxext-rediraffe
rediraffe_redirects = "redirects.txt"
rediraffe_branch = "master~1"

htmlhelp_basename = "confuciangentlemansclubdoc"

latex_elements = {}

latex_documents = [
    (
        "index",
        "confuciangentlemansclub.tex",
        "confucian gentleman's",
        "Tony Narlock",
        "manual",
    ),
]

man_pages = [
    (
        "index",
        "confuciangentlemansclub",
        "confucian gentleman's club",
        ["Tony Narlock"],
        1,
    )
]

texinfo_documents = [
    (
        "index",
        "confuciangentlemansclub",
        "confucian gentleman's club",
        "Tony Narlock",
        "confuciangentlemansclub",
        "Scribe.",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "tmuxp": ("https://tmuxp.git-pull.com/", None),
    "libtmux": ("https://libtmux.git-pull.com/", None),
    "libvcs": ("https://libvcs.git-pull.com/", None),
    "vcspull": ("https://vcspull.git-pull.com/", None),
    "cihai": ("https://cihai.git-pull.com/", None),
    "cihai-cli": ("https://cihai-cli.git-pull.com/", None),
    "unihan-etl": ("https://unihan-etl.git-pull.com/", None),
    "unihan-db": ("https://unihan-db.git-pull.com/", None),
    "gp-libs": ("https://gp-libs.git-pull.com/", None),
    "django-docutils": ("https://django-docutils.git-pull.com/", None),
    "django-slugify-processor": (
        "https://django-slugify-processor.git-pull.com/",
        None,
    ),
    "django": (
        "https://docs.djangoproject.com/en/4.1/",
        "https://docs.djangoproject.com/en/4.1/_objects/",
    ),
}


def remove_tabs_js(app: "Sphinx", exc: Exception) -> None:
    # Fix for sphinx-inline-tabs#18
    if app.builder.format == "html" and not exc:
        tabs_js = pathlib.Path(app.builder.outdir) / "_static" / "tabs.js"
        tabs_js.unlink(missing_ok=True)


def setup(app: "Sphinx") -> None:
    app.connect("build-finished", remove_tabs_js)
