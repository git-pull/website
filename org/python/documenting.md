# Documenting

## Sphinx

### Docutils

Sphinx is built on top of docutils.

```{admonition} docutils: Documentation parser

- Homepage: <https://docutils.sourceforge.io/>
- Repo: <https://docutils.sourceforge.io/docs/dev/repository.html>
- PyPI: <https://pypi.org/project/docutils/>
- Changes: <https://docutils.sourceforge.io/RELEASE-NOTES.html>
```

### Markdown

Markdown support is through docutils and [MyST-Parser](https://myst-parser.readthedocs.io/)

```{admonition} MyST-Parser: Markdown plugin for docutils

- Homepage: <https://myst-parser.readthedocs.io/>
- Repo: <https://github.com/executablebooks/MyST-Parser>
- PyPI: <https://pypi.org/project/myst-parser/>
- Changes: <https://myst-parser.readthedocs.io/>
```

### Furo theme

All git-pull projects use pradyunsg's [Furo] theme.

```{admonition} furo: Sphinx theme

- Homepage: <https://pradyunsg.me/furo/quickstart>
- Repo: <https://github.com/pradyunsg/furo>
- PyPI: <https://pypi.org/project/furo/>
- Changes: <https://pradyunsg.me/furo/changelog/>
```

[furo]: https://github.com/pradyunsg/furo

### API Documentation

We document all APIs in our projects via `sphinx.ext.autodoc`. This automatically outputs our
modules in a neat way, which is even compatible to oth other python projects via
`sphinx.ext.intersphinx`.

#### `doctest` (in docstrings)

In `.py` modules, we use `doctest` examples of function, class and method use within docs for
explanatory and test coverage purposes. These also turn into helpful, copyable code down the line.

### Examples

#### Files

Files that are included in docs, e.g. via `.. include::`, such as `.json`, `.yaml`, `.py` should be
tested in `tests/` as part of the CI workflow to ensure those work across releases.

#### `doctest` (inside docs)

We use `doctest` for our examples

This ensures that even across changes, documentations are still functioning.

It also adds coverage and ensures our libraries and applications work as the user would expect.
