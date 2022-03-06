# Structure of Python Projects

Want to contribute to a git-pull project? They follow a common layout. This guide can help you make
sense of things!

tmuxp, libtmux, cihai, libvcs, vcspull, and others follow common patterns in their layout.

## Styling

[black][black] is used for code formatting.

The max line length is 88 (compared to PEP8's 79). `flake8: noqa` is permitted for docstrings where
it's too long.

Use `$ make black` to run your code through black.

Use `$ make flake8` to validate compliance with the project's code standards.

[black]: https://github.com/ambv/black

## Dependencies

### Traditional requirements files

_requirements/_ - dependencies, for backwards support on systems not using [pipenv][pipenv]

Not all projects may have these. If they don't require third party dependencies in the main project,
e.g. SQLAlchemy or colorama, then their may be no _base.txt_.

_requirements/base.txt_ - Direct project dependencies. These things are included in the
`install_requires` in _setup.py_, so they're invoked via `python setup.py install`.

_requirements/test.txt_ - Test packages. Examples: pytest, pytest-rerunfailures. These can be
included via `test_requires` in setup.py, so they're invoked via `python setup.py test`.

As of June 2018, our projects also use [pyup.io][pyup.io] for automated package updates. These don't
support _Pipfile_ yet, so that's another reason we're not moving over to Pipfile immediately.

### Pipfile

[pipenv][pipenv] supports installing via a _Pipfile_:

```
$ pipenv install --dev --skip-lock
```

Our projects don't use the _Pipfile.lock_ since they can cause issues with dependencies / version
constraints and has a performance penalty.

To keep a _Pipfile_ up to date, you can do some combination of the following:

```{code-block} sh

pipenv install --skip-lock --dev -r requirements/doc.txt && \
pipenv install --skip-lock --dev -r requirements/dev.txt && \
pipenv install --skip-lock --dev -r requirements/test.txt && \
pipenv install --skip-lock -r requirements/base.txt

```

Some projects may create a Make task for it in the _Makefile_:

```{code-block} make

sync_pipfile:
    pipenv install --skip-lock --dev -r requirements/doc.txt && \
    pipenv install --skip-lock --dev -r requirements/dev.txt && \
    pipenv install --skip-lock --dev -r requirements/test.txt && \
    pipenv install --skip-lock -r requirements/base.txt

```

## Optional development tools

## tmuxp

You can automatically launch and IDE-like terminal session from [tmux][tmux] via [tmuxp][tmuxp] and
the includes _.tmuxp.yaml_ file. These functionality will automatically handle dependencies via
[pipenv][pipenv]

## Make tasks

[make(1)][make(1)] is a popular utility on POSIX-like systems to save common commands across
codebases/checkouts. For convenience, these can be stored in tasks in _Makefile_ to prevent
unnecessary repetition.

To ensure uniformity and max interoperability across developer systems, [Make][make] tasks are used.
In addition, makefiles make use of variables via command concatenation to find / filter source files
across different platforms.

### _Makefile_

Variable example:

```{code-block} make

PY_FILES= find . -type f -not -path '*/\.*' | grep -i '.*[.]py$$' 2> /dev/null

```

This is uses [find(1)][find(1)] and [grep(1)][grep(1)] options tested to work across BSD, macOS,
Linux to scan files recursively (in nested directories), and also filter them. For instance,
`-f -not -path '*/\.*` ignore files beginning with a dot, e.g. `.env`, and grep's `-i '.*[.]py$$'`
filters for only `*.py` files. The double `$$` is used to escape the `$`. In regular expressions, a
`$` is used to represent the end of a string.

### _doc/Makefile_

Sphinx documentation tasks.

Variable example:

```{code-block} make

WATCH_FILES= find .. -type f -not -path '*/\.*' | grep -i '.*[.]rst\|CHANGES\|TODO\|.*conf\.py\|.*[.]py$$' 2> /dev/null

```

Will be used to generate a list of files to monitor for changes. This uses `find ..` to look a
directory behind `./doc` (`../doc` is the project root). It will monitor for `*.rst` and `*.py`
files (python files have code documentation) and also for `CHANGES` and `TODO` (which include
reStructuredTest, but lack file extensions for legacy purposes.)

```{code-block} make

PYVERSION=$(shell python -c "import sys;v=sys.version_info[0];sys.stdout.write(str(v))")

```

Is used for version checks. It is a uniform and tested way to find the major python version (`2` or
`3`), since they used a different module to serve HTTP files:

```{code-block} make

WATCH_FILES= find .. -type f -not -path '*/\.*' | grep -i '.*[.]rst\|CHANGES\|TODO\|.*conf\.py\|.*[.]py$$' 2> /dev/null
PYVERSION=$(shell python -c "import sys;v=sys.version_info[0];sys.stdout.write(str(v))")
HTTP_PORT     = 8031

serve:
    @echo '=============================================================='
    @echo
    @echo 'docs server running at http://0.0.0.0:${HTTP_PORT}/_build/html'
    @echo
    @echo '=============================================================='
    @if test ${PYVERSION} -eq 2; then $(MAKE) serve_py2; else make serve_py3; fi

serve_py2:
    python -m SimpleHTTPServer ${HTTP_PORT}

serve_py3:
    python -m http.server ${HTTP_PORT}

```

Task example: `make watch`

## pytest

pytest is used for testing, instead of standard library's [unittest][unittest].

They reside in the project root, inside of the _tests/_ folder. Test files are kept in
_test\_{subject_name}.py_. In addition, helper modules of any name (e.g. _helper.py_) are permitted,
in addition to the use of _conftest.py_ (which is used by [pytest's fixture][pytest's fixture]
system)

## _setup.py_

What you'll find in a _setup.py_ file.

### requirements.txt integration

_requirements.txt_ / _requirements/base.txt_ for `install_requires` _requirements/test.txt_ for
`install_requires`

### pytest integration

Overrides `python setup.py test` with a custom class:

```{code-block} python

from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)
setup(
    # ... stuff
    cmdclass={'test': PyTest},
)

```

[pipenv]: https://docs.pipenv.org/
[make]: https://en.wikipedia.org/wiki/Make_(software)
[pytest]: https://pytest.org
[unittest]: https://docs.python.org/3/library/unittest.html
[tmux]: https://github.com/tmux/tmux/wiki
[tmuxp]: https://tmuxp.git-pull.com
[make(1)]: https://linux.die.net/man/1/make
[find(1)]: https://linux.die.net/man/1/find
[grep(1)]: https://linux.die.net/man/1/grep
[pytest's fixture]: https://docs.pytest.org/en/latest/fixture.html
[pyup.io]: https://pyup.io/
