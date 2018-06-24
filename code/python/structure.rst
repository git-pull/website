Structure of Python Projects
============================

Want to help in a git-pull project? They follow a common layout,
this guide is to help you make sense of things!

tmuxp, libtmux, cihai, libvcs, vcspull, and others follow
common patterns in their layout.

Dependencies
------------

Traditional requirements files
""""""""""""""""""""""""""""""

*requirements/* - dependencies, for backwards support on systems
not using `pipenv`_

Not all projects may have these. If they don't require third party
dependencies in the main project, e.g. SQLAlchemy or colorama, then
their may be no *base.txt*.

*requirements/base.txt* - Direct project dependencies. These things
are included in the ``install_requires`` in *setup.py*, so they're
invoked via ``python setup.py install``.

*requirements/test.txt* - Test packages. Examples: pytest,
pytest-rerunfailures. These can be included via ``test_requires``
in setup.py, so they're invoked via ``python setup.py test``.

As of June 2018, our projects also use `pyup.io`_ for automated
package updates. These don't support *Pipfile* yet, so that's
another reason we're not moving over to Pipfile immediately.

Pipfile
"""""""

`pipenv`_ supports installing via a *Pipfile*::

    $ pipenv install --dev --skip-lock

Our projects don't use the *Pipfile.lock* since they can cause
issues with dependencies / version constraints and has a performance
penalty.

To keep a *Pipfile* up to date, you can do some combination of
the following:

.. code-block:: sh

    pipenv install --skip-lock --dev -r requirements/doc.txt && \
    pipenv install --skip-lock --dev -r requirements/dev.txt && \
    pipenv install --skip-lock --dev -r requirements/test.txt && \
    pipenv install --skip-lock -r requirements/base.txt

Some projects may create a Make task for it in the *Makefile*:

.. code-block:: make

    sync_pipfile:
        pipenv install --skip-lock --dev -r requirements/doc.txt && \
        pipenv install --skip-lock --dev -r requirements/dev.txt && \
        pipenv install --skip-lock --dev -r requirements/test.txt && \
        pipenv install --skip-lock -r requirements/base.txt

Optional development tools
--------------------------

tmuxp
-----

You can automatically launch and IDE-like terminal session from `tmux`_
via `tmuxp`_ and the includes *.tmuxp.yaml* file. These functionality
will automatically handle dependencies via `pipenv`_

Make tasks
----------

There are many utility commands which are commonly used but require a lot of 
remembering / typing. For convenience, these can be stored in tasks in
*Makefile* to prevent unnecessary repetition.

To ensure uniformity and max interoperability across developer systems, `Make`_ 
tasks are used. In addition, makefiles make use of variables via command 
concatenation to find / filter source files across different platforms.

*Makefile*
""""""""""

*Variables*: Example is ``PY_FILES= find . -type f -not -path '*/\.*' |
grep -i '.*[.]py$$' 2> /dev/null``. This is uses `find(1)`_ and `grep(1)`_
options tested to work across BSD/macOS/Linux to scan files recursively
(in nested directories), and also filter them. For instance, ``-f -not -path
'*/\.*`` ignore files beginning with a dot, e.g. ``.env``, and grep's
``-i '.*[.]py$$'`` filters for only ``*.py`` files. The double ``$$`` is
used to escape the ``$``. In regular expressions, a ``$`` is used to
represent the end of a string.


*doc/Makefile*
""""""""""""""

Sphinx documentation tasks.

Variables inside:

``WATCH_FILES= find .. -type f -not -path '*/\.*' | grep -i '.*[.]rst\|CHANGES\|TODO\|.*conf\.py\|.*[.]py$$' 2> /dev/null``

Will be used to generate a list of files to monitor for changes. This uses
``find ..`` to look a directory behind ``./doc`` (``../doc`` is the project root).
It will monitor for ``*.rst`` and ``*.py`` files (python files have code
documentation) and also for ``CHANGES`` and ``TODO`` (which include
reStructuredTest, but lack file extensions for legacy purposes.)

``PYVERSION=$(shell python -c "import sys;v=sys.version_info[0];sys.stdout.write(str(v))")``

Is used for version checks. It is a uniform and tested way to find the
major python version (``2`` or ``3``), since they used a different module
to serve HTTP files:

.. code-block:: make

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

Task example: ``make watch``

pytest
------

pytest is used for testing, instead of standard library's `unittest`_.

They reside in the project root, inside of the *tests/* folder. Test
files are kept in *test_{subject_name}.py*. In addition, helper modules
of any name (e.g. *helper.py*) are permitted, in addition to the use
of *conftest.py* (which is used by `pytest's fixture`_ system)

.. _pipenv: https://docs.pipenv.org/
.. _Make: https://en.wikipedia.org/wiki/Make_(software)
.. _pytest: https://pytest.org
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _tmux: https://github.com/tmux/tmux/wiki
.. _tmuxp: https://tmuxp.git-pull.com
.. _make(1): https://linux.die.net/man/1/make
.. _find(1): https://linux.die.net/man/1/find
.. _grep(1): https://linux.die.net/man/1/grep
.. _pytest's fixture: https://docs.pytest.org/en/latest/fixture.html
.. _pyup.io: https://pyup.io/
