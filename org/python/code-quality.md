(python-code-quality)=

# Code quality

The ecosystem we reside in enjoys the benefit of well-developed tooling to ensure code is:

- Formatted uniformly (and automatically)
- Imports are sorted
- Types are correct
- Anything left is caught by flake8's rules

These offer our first line of defense to catch bugs or that something's out of place, before a test
is even ran.

What's nice about these tools is {ref}`text editors and IDEs supporting python <python-text-editor>`
can integrate with them and even detect our configurations.

## Type safety

### mypy

All git-pull projects use [mypy].

mypy makes:

- refactorings easier
- catches bugs
- provides downstream type annotations

```{admonition} mypy: Static type checker

- Homepage: <http://mypy-lang.org/>
- Repo: <https://github.com/python/mypy8>
- PyPI: <https://pypi.org/project/mypy/>
- Changes: <http://mypy-lang.org/news.html>
```

#### mypy strictness

In addition, most projects - include libtmux, libvcs, unihan-etl, are either using `--strict` or on
a trajectory toward being so.

[mypy]: https://github.com/python/mypy

## Linting

### flake8

```{admonition} flake8: Linter

- Homepage: <https://flake8.pycqa.org/>
- Repo: <https://github.com/PyCQA/flake8>
- PyPI: <https://pypi.org/project/flake8/>
- Changes: <https://flake8.pycqa.org/en/latest/release-notes/index.html>
```

#### flake8 extensions

- flake8-bugbear ([repo](https://github.com/PyCQA/flake8-bugbear))
- flake8-comprehensions ([repo](https://github.com/adamchainz/flake8-comprehensions))

## Formatting

### black

```{admonition} black: Formatter

- Homepage: <https://black.readthedocs.io/en/stable/>
- Repo: <https://github.com/psf/black>
- PyPI: <https://pypi.org/project/black/>
- Changes: <https://github.com/psf/black/blob/main/CHANGES.md>
```

### isort

```{admonition} isort: Import sorter

- Homepage: <https://pycqa.github.io/isort/>
- Repo: <https://github.com/PyCQA/isort>
- PyPI: <https://pypi.org/project/isort8/>
- Changes: <https://pycqa.github.io/isort/CHANGELOG.html>
```

## Modernizing python code

From time to time projects can benefit from cleaner syntax of newer python versions. When we do
this, we always maintainer support for the minimum python version (this is seen in the
`pyproject.toml`)
