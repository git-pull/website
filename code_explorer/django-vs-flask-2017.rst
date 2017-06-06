.. _django-vs-flask-2017:

=============================
Django vs Flask: 2017 Edition
=============================
Which is better
===============

I have used both extensively and have want to want to save technical decision
makers time.

Since this is 2017, I had to grab the latest Flask to refresh my memory
and see what's changed. But let's keep this going every year.

TLDR
====

Use Django.

B-b-but-what? Keep reading. I'll cover both extensively. And I'm not
saying Flask is bad, but you'll miss the things a full fledge framework provides
for you. Django's extension community is more active. Django's ORM, while
different than SQLAlchemy (which is often paired with Flask), is superb. You're
going to end up reinventing the wheel to catch up for things that'd otherwise be
quick wins with Django.

As of 2017, I am partial to using Django. In the past, I was intensely
devoted to Flask and SQLAlchemy due to its API documentation and pythonics.

Django
======

Today, Django is built and maintained by the open source community. The initial
release was July 21, 2005, by Lawrence Journal-World.

What Django provides
--------------------

- :django:ref:`Template Engine <templates>`

  - Filters
  - Tags
  - Context preprocessor middleware (global, per-request :py:class:`dict` passed
    into templates)
- ORM

  - QuerySet (reuseable object used in ORM-backed features)
  - Migrations
  - Raw Queries
- Forms

  - Fields
  - Widgets
  - ModelForm (ORM-backed forms)
- Views

  - Class-based views

    - DetailView, ListView (ORM-backed views)
- URL routing
- Administration web interface (ORM-backed CRUD backend)
- Authentication

  - User model
  - Basic permission systems
- Caching
- Modularity via Apps
- Settings, configurable via ``DJANGO_SETTINGS_MODULE``
- Command system
- Shell
- Static file support

Extending Django
----------------

Django has a vibrant third-party development community. Apps are installed
via appending them to the ``INSTALLED_APPS`` in the settings.

Popular Django extensions include:

- REST: `Django REST Framework`_, aka "DRF"
- Permissions: `django-guardian`_
- Asset pipelines: `django-compressor`_, `django-webpack-loader`_
- Debugging, Miscellaneous: `django-extensions`_, `django-debug-toolbar`_

.. _Django REST Framework: http://www.django-rest-framework.org/
.. _django-guardian: https://django-guardian.readthedocs.io/
.. _django-compressor: https://django-compressor.readthedocs.io/
.. _django-webpack-loader: https://github.com/ezhome/django-webpack-loader
.. _django-extensions: https://django-extensions.readthedocs.io/
.. _django-debug-toolbar: https://django-debug-toolbar.readthedocs.io/

Flask
=====

Like Django, Flask is also built and maintained in the open source
community. The creator of the software itself is Armin Ronacher. Initial
release April 1, 2010.

What Flask provides
-------------------

- Template system via jinja2
- URL routing via Werkzeug
  - Mountable URL's via blueprints
- Modularity via blueprints

Extending Flask
---------------

Since Flask doesn't include things like an ORM, authentication and access
control, it's up to the user to include libraries to handle those a la
carte.

It's often paired with SQLAlchemy. You can also use Peewee ORM.

Popular Flask extensions include:

- REST: `flask-restful`_ (`flask-restful-swagger`_)
- Admins: `Flask-Admin`_ `Flask-SuperAdmin`_
- Auth: `flask-login`_, `flask-security`_

.. _flask-restful: https://flask-restful.readthedocs.io/
.. _flask-restful-swagger: https://github.com/rantav/flask-restful-swagger
.. _Flask-Admin: https://github.com/flask-admin/flask-admin
.. _Flask-SuperAdmin: https://github.com/SyrusAkbary/Flask-SuperAdmin
.. _flask-login: https://flask-login.readthedocs.io/
.. _flask-security: https://flask-security.readthedocs.io

Further python dependencies you'll pull in, not necessarily dependent on
Flask:

- Social authentication: `authomatic`_, `python-social-auth`_
- Forms: `WTForms`_
- RDBMS: `SQLAlchemy`_, `peewee`_
- Mongo: `MongoEngine`_

For more, see `awesome-flask`_ on github.

.. _python-social-auth: https://github.com/omab/python-social-auth
.. _authomatic: https://github.com/authomatic/authomatic
.. _WTForms: https://wtforms.readthedocs.io
.. _MongoEngine: http://docs.mongoengine.org/
.. _SQLAlchemy: https://sqlalchemy.org
.. _peewee: http://docs.peewee-orm.com/

.. _awesome-flask: https://github.com/humiaozuzu/awesome-flask

Configuring Flask
-----------------

Flask is configured via an object.

Flask's Initialization
----------------------

Since Flask doesn't include database models,

Flask and Databases
-------------------

Unlike Django, Flask doesn't tie you to a database.

There's no rules saying your Flask app has to connect to a database. You're
writing python, you could be using flask to make a proxy/abstraction of someone
else's REST API. Or for a quick web front-end to a purely python program you're
making.

You could end up generating a purely static website with no SQL backend `a la NPR`_.

But it's most likely you'll be using SQLAlchemy. A common combination is
to use it with `flask-sqlalchemy <http://http://flask-sqlalchemy.pocoo.org/>`_.

.. _a la NPR: http://blog.apps.npr.org/2014/07/29/everything-our-app-template-does.html

Interpretations
===============

Flask is pure, but you'll always be missing something
-----------------------------------------------------

The one thing that strikes me about Flask is it's really meant to stay out
of your way. The API is, much like this website, documented in sphinx,
it's straight-forward and puts code first.

Django is comprehensive, solid, active, customizable, and robust
----------------------------------------------------------------

:django:ref:`Batteries included <tut-batteries-included>`.

A deep notion of customizability and using your own Field, Forms, Class
Based Views, and so on to suit situations where need that.

The parts fit together with Django. And you'll need them.

From the :class:`~django:django.db.models.query.QuerySet`

Open source momentum
--------------------

Flask, as a microframework, is relatively dormant from an activity
standpoint (after all, what are you really going to add to something meant
to be small). It's not about stars, or commits, or contributor count. It's
about features you can articulate in a `change log <https://github.com/pallets/flask/blob/master/CHANGES>`_.

The good news is, Flask isn't getting bloated. Recent pull requests seem
to be on tweaking and refining facilities that are already present.

Meanwhile, Django wants to do everything web. And everything fits together.
And it needs to, because it's a framework. And since it covers so much
ground, let's try to put it into proportion:

- Django ORM -> SQLAlchemy
- Django Templates -> Jinja2
- Django Core / URL's -> Werkzeug

There are also feature requests that come in, often driven by need of the
web development community, and things that otherwise wouldn't be
considered for Flask or Flask extension. Which kind of hurts open source,
because there's code that could be reuseable being written, but not worth
the effort to make an extension for. So there are `snippets
<http://flask.pocoo.org/snippets/>`_ for that.

Suggestions -- Points to consider
=================================
Beware the purity trap
----------------------

The idea of having your python script there and being able to not tie in a
whole framework is tempting.

Further, being able to keep data models inert, so python scripts as well
as a web app can both pull them inside, is good programming.

By being so philosophically pure and pythonic, you'll save time in the long run.
All the great virtues of ``import this``.

Code that does too much to be "pure" or "correct" nearly never scales.

I feel the same attitude toward a certain other programming language, as
well as an operating system. `Too much pride gets invested in identity
<http://www.paulgraham.com/identity.html>`_.

A couple of anecdotes of my own, in the spirit of `Burke and Wills ill-fated expedition <https://en.wikipedia.org/wiki/Burke_and_Wills_expedition>`_:

Anecdote: Pursuit of JS Holy Grail
""""""""""""""""""""""""""""""""""

In 2014, I remember wanting to be able to re-use code on the front-end and
back-end. So I opted to pick up Node.js. While I was able to use the same
templates. In search of the "Holy Grail". It turned out, Node.js was a
nightmare for scaling code at the time. When you're reusing behavior, middleware
functions are not a replacement for OOP. Having to wrap everything in promises.
In addition, we were left to our own getting validation on forms and REST
endpoints to work. It all had to be done by hand. After what months of begging,
I finally encouraged the supervisor to let us switch to Django. It rescued us.

(Not knocking node.js, I still use it and since 2014, it's grown a lot)

Anecdote: Pursuit of the Pythonic Holy Grail
""""""""""""""""""""""""""""""""""""""""""""

The other for me, was Flask and SQLAlchemy. Flask had a super fast
template engine. Straight-forward modularization with blueprints. Works
well with python code you have on standby. SQLAlchemy `is in AOSA 
<http://aosabook.org/en/sqlalchemy.html>`_ (*The Architecture of Open
Source Applications*). And the way it builds on top of that layer of core
commands. Brilliant architecture.

So at the end of the day, the reality is, the (relatively) simpler
solution provided by Django wins. Thanks to Django's features and third
party extensions all plugging into :class:`~django:django.db.models.query.QuerySet`,
everything ends up being consistent. No such plugin community of similar
size and activity exists for SQLAlchemy's :class:`~sqlalchemy:sqlalchemy.orm.query.Query`

Also ultimately, I wanted to have a declarative way to plug in blueprints
(what django calls apps). So I ended up having a yaml file to specifying
the python string path to the blueprints. And also, I even go so far as to
scan for model classes and inject DB metadata into them. So basically, I'm
recreate Django. And finally, I grab WTForms to do what django.forms does,
and find that it's nowhere near as straight forward as what Django would
give me out of the box.

By the way, I still use SQLAlchemy on projects. And who knows, maybe next
year the contrib community with Flask will forge forward. Anything's
possible. I want to pick the best tool for the job, and if thing's change
I promise to update.

Conclusion
==========

I think Flask is great for a quick web app, particularly for a python
script you just want a front-end for.

If you already are using SQLAlchemy models, you can get them working with
your Flask application with little work. With Flask, you feel in control.

Once you begin implementing a database backend, however, I felt Flask entered
a cycle of diminishing returns. Before long, you'll be dealing with forms, REST
endpoints and other things that are all best represented via a declarative model
with types. Which is kind of the philosophy Django's Apps do from the
start.

There's an information perception that batteries included may mean a growing
list of ill-maintained API's that get hooked into every request. In the
case of Django, everything works across the board. If one API updates, you
can expect Django's testsuites to break and the appropriate changes are
made. So stuff integrates. This is something that's harder to do when you
have a lot of packages from different authors you have to wait to cut a
release in Flask's ecosystem.

And if things change. I look forward to it. Despite Flask's success, and missing
out on Django's synergy, it is still a mighty, mighty microframework.

Bonus: How do I learn Django or Flask?
--------------------------------------

Preparation:

- Understand how python `virtual environments`_ (see `Real Python
  <https://realpython.com/blog/python/python-virtual-environments-a-primer/>`_'s
  tutorial) and PATH's work. This is an absolute must. Also, check out my
  book *The Tao of tmux* `available online free
  <https://leanpub.com/the-tao-of-tmux/read>`_ for some good coverage of
  the terminal.
- Grab Django's documentation `PDF
  <https://media.readthedocs.org/pdf/django/latest/django.pdf>`_ and Flask's
  documentation, `PDF
  <http://flask.pocoo.org/docs/dev/.latex/Flask.pdf>`_. Read it on a tablet.
- In your spare time, get in the habbit of reading python docs on
  ReadTheDocs.org (a documentation hosting website) and 

Developing:

- Make a hobby website in django or flask. Try hosting it on something
  like `Heroku`_, which is free and has simple deployments. Also,
  DigitalOcean plans `start at $5/mo <https://m.do.co/c/a8d3c8586c91>`_.
- Bookmark and study to this article to get the latest on differences
  between Django and Flask. While it's a comparison, it'll be helpful in
  curating the API and extension universe they have.
- For free editors, check out good old `vim`_ + `python-mode`_, `Visual Studio 
  Code`_, `Atom`_, or `PyCharm`_

.. _Heroku: https://www.heroku.com/
.. _virtual environments: https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/
.. _python-mode: https://github.com/python-mode/python-mode
.. _vim: http://www.vim.org
.. _Visual Studio Code: https://code.visualstudio.com/
.. _Atom: https://atom.io/
.. _PyCharm: https://www.jetbrains.com/pycharm/

Hire me
=======

Looking to hire a Flask or Django developer remote? Teacher? Send me an email, tony
at git-pull.com.

Like my stuff? :ref:`Your support is appreciated! <support>`

