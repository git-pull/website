.. _python_packaging_modules_cyclic:

==========================================================
Python packaging, relative modules and cyclic dependencies
==========================================================

Take a look at flask, pip


Inside their own modules, flask:

Let's look at `flask/__init__.py`_::

    # utilities we import from Werkzeug and Jinja2 that are unused
    # in the module but are exported as public interface.
    from werkzeug.exceptions import abort
    from werkzeug.utils import redirect
    from jinja2 import Markup, escape

    from .app import Flask, Request, Response
    from .config import Config
    from .helpers import url_for, flash, send_file, send_from_directory, \
        get_flashed_messages, get_template_attribute, make_response, safe_join, \
        stream_with_context
    from .globals import current_app, g, request, session, _request_ctx_stack, \
         _app_ctx_stack
    from .ctx import has_request_context, has_app_context, \
         after_this_request, copy_current_request_context
    from .module import Module
    from .blueprints import Blueprint
    from .templating import render_template, render_template_string

    # the signals
    from .signals import signals_available, template_rendered, request_started, \
         request_finished, got_request_exception, request_tearing_down, \
         appcontext_tearing_down, appcontext_pushed, \
         appcontext_popped, message_flashed

.. _flask/__init__.py: https://github.com/mitsuhiko/flask/blob/master/flask/__init__.py


https://github.com/mitsuhiko/flask/blob/master/flask/ctx.py is importing
relatively with names::

    from werkzeug.exceptions import HTTPException

    from .globals import _request_ctx_stack, _app_ctx_stack
    from .module import blueprint_is_module
    from .signals import appcontext_pushed, appcontext_popped

I heard before its best practice to just import the module and access it
namespaced.

Pip `pip.__init__.py`_::

    #!/usr/bin/env python
    import os
    import optparse

    import sys
    import re

    from pip.exceptions import InstallationError, CommandError, PipError
    from pip.log import logger
    from pip.util import get_installed_distributions, get_prog
    from pip.vcs import git, mercurial, subversion, bazaar  # noqa
    from pip.baseparser import ConfigOptionParser, UpdatingDefaultsHelpFormatter
    from pip.commands import commands, get_summaries, get_similar_command

.. _pip.__init__.py: https://github.com/pypa/pip/blob/develop/pip/__init__.py

Look at the top of `pip.log`_::

    ""Logging
    """

    import sys
    import os
    import logging

    import pkg_resources

    from pip import backwardcompat
    from pip._vendor import colorama

Where `pip.backwardcompat`_ is a module.

.. _pip.log: https://github.com/pypa/pip/blob/develop/pip/log.py
.. _pip.backwardcompat: https://github.com/pypa/pip/blob/develop/pip/backwardcompat/__init__.py


Wrap your brain around this concept.

This is not an applied application being used for a personal project, this
is a proper package that stands on its own. It's Flask.

Look at ``__init__``.

Software development with time constrictions may not permit every project
to be module, but for software that goes up on pypi or gets reused at
work, adhering to good architecture will save time.
