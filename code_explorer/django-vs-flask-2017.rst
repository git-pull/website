.. _django-vs-flask-2017:

=============================
Django vs Flask: 2017 Edition
=============================
Which is better
===============

I consider myself a strong Django and Flask developer. Having used both
extensively, I want to offer information and insight for technical decision
makers.

I'd pick Django 9/10 times.

B-b-but-what? Keep reading. I'll cover both extensively. And I'm not
saying Flask is bad, but you'll miss the things a full fledge framework provides
for you. Django's extension community is more active. Django's ORM, while
different than SQLAlchemy (which is often paired with Flask), is superb. You're
going to end up reinventing the wheel to catch up for things that'd otherwise be
quick wins with Django.

Django
======

Today, Django is built and maintained by the open source community. The initial
release was July 21, 2005, by Lawrence Journal-World.

What Django provides
--------------------

- :doc:`Template Engine <django:ref/templates/index>`

  - :django:ref:`Filters <filters>`
  - :django:ref:`Tags <tags>`
  - :django:ref:`Context preprocessor middleware <subclassing-context-requestcontext>`
    (global, per-request :py:class:`dict` passed into templates)
- :doc:`ORM <django:topics/db/models>`

  - :class:`~django:django.db.models.query.QuerySet` (reuseable object used in ORM-backed features)
  - :doc:`Migrations <django:topics/migrations>`
  - :doc:`Raw Queries <django:topics/db/sql>`
- :doc:`Forms <django:topics/forms/index>`

  - :doc:`Fields <django:ref/forms/fields>`
  - :doc:`Widgets <django:ref/forms/widgets>`
  - :doc:`Forms <django:topics/forms/modelforms>` (ORM-backed forms)
- :doc:`Views <django:topics/http/views>`

  - :doc:`Class-based views <django:topics/class-based-views/index>`

    - :class:`~django:django.views.generic.detail.DetailView`,
      :class:`~django:django.views.generic.list.ListView` (ORM-backed views)
- :doc:`URL routing <django:topics/http/urls>`
- :doc:`Administration web interface <django:ref/contrib/admin/index>`
  (ORM-backed CRUD backend)
- :doc:`Authentication <django:topics/auth/index>`

  - :class:`~django:django.contrib.auth.models.User` model
  - :django:ref:`Basic permission systems <topic-authorization>`
- :doc:`Caching <topics/cache>`
- :doc:`Multi-tenancy <django:ref/contrib/sites>` via domain
- :doc:`Modularity via Apps <django:ref/applications>`
- :doc:`Settings <django:topics/settings>`, configurable via ``DJANGO_SETTINGS_MODULE``
- :doc:`Command system <django:ref/django-admin>`

  - Shell with automatic integration of `bpython`_ and `ipython`_, if detected
  - Launch DB command-line client (psql, mysql, sqlite3, sqlplus) based on engine configuration in settings.
  - :doc:`Custom commands <django:howto/custom-management-commands>`
- :doc:`Static file support <django:howto/static-files/index>`

.. _bpython: https://bpython-interpreter.org/
.. _ipython: https://ipython.org/

Extending Django
----------------

Django has a vibrant third-party development community. Apps are installed
via appending them to the ``INSTALLED_APPS`` in the settings.

Popular Django extensions include:

- REST: `Django REST Framework`_, aka "DRF"
- Permissions: `django-guardian`_
- Asset pipelines: `django-compressor`_, `django-webpack-loader`_
- Debugging, Miscellaneous: `django-extensions`_, `django-debug-toolbar`_
- Filtering / Search: `django-filter`_
- Tabular / paginated output of db: `django-tables2`_

.. _Flask-SQLAlchemy: http://flask-sqlalchemy.pocoo.org/
.. _Django REST Framework: http://www.django-rest-framework.org/
.. _django-guardian: https://django-guardian.readthedocs.io/
.. _django-compressor: https://django-compressor.readthedocs.io/
.. _django-webpack-loader: https://github.com/ezhome/django-webpack-loader
.. _django-extensions: https://django-extensions.readthedocs.io/
.. _django-debug-toolbar: https://django-debug-toolbar.readthedocs.io/
.. _django-filter: https://django-filter.readthedocs.io/
.. _django-tables2: https://django-tables2.readthedocs.io/

Customizing Django
------------------

Eventually the included forms, fields and class-based views included in
Django aren't going to be enough. 

The fear of framework dependencies
----------------------------------

There's a well-advised stigma pre-fabricated solutions don't work in the
long term.

Many buy commercial HTML/CSS themes just to throw them away it doesn't work with
your setup. Then the real beauty of the template is gone. Others rely on CMS and
forum software and aren't able to convey data how they wish, so they're stuff
with whatever prefabricated systems exist.

Django is not a CMS. The aspects django occupies are:

- mapping data out via objects (ORM models)
- presenting data (templates)
- mapping patterns of URL regular expressions (urls.py) to business logic
  (views)
- making request (GET, PUT, session stuff) information accessible 
- environmental configuration (settings) and an environment variables
  (``DJANGO_SETTINGS_MODULE``) e.g. dev, staging, prod workflows
  
A tool kit of web abstractions that solve proven, repeated problems in the trade.

Rather than being Django's achille heel, Django's saving grace is the
standard building blocks being ammenable to highly granular changes.

It's also where Django's programming language, python, gives a big boost.

Django uses classes right
"""""""""""""""""""""""""

While python isn't statically typed, its inheritance hierarchy is very
straight-forward and navigable.

.. seealso::
  
    Free tools in the community such as `jedi`_ provide navigation of modules,
    functions and classes to editors like vim and atom.

Used incorrectly, :python:ref:`tut-classes` makes code harder to read and
maintain. Needless abstraction sucks the air out of projects.

By contrast, when used pragmatically, they're a pleasure to implement downstream
and reuse. Notably, Django's :doc:`django:topics/class-based-views/index` which
shipped in :doc:`Django 1.3 <django:releases/1.3>`.


Retrofit the batteries
""""""""""""""""""""""

Re

.. _jedi: http://jedi.readthedocs.io/

Configuring Django
------------------

``DJANGO_SETTINGS_MODULE`` maps a string to a module in your current
environment's python packages.

.. warning:: Understand virtualenvs or fail
   
   When developing: if you're not sourced in a virtual enviroment in a shell, your
   settings module (and probably the django module itself) won't be found.
   
   When deploying: not including your site-packages in your uwsgi
   configuration, you also won't find django or your settings.

   This is the single biggest learning barrier python has. It will hinder you
   every step of the way until you wrap your brain around it.

Django's intialization
----------------------

1. Django checks for your ``DJANGO_SETTINGS_MODULE`` and parses the file

   This is where all your database, installed applications and other stuff
   comes from.

   Even if you're not using the server and just using addons, Django needs
   this to display available commands via ``./manage.py``.

   If settings module is found and correct. Move to next step.

2. Load apps and their models

3. Run verification checks against models to :doc:`assure nothing's broken
   <django:ref/checks>` (since :doc:`Django 1.7 <django:releases/1.7>`)

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

Popular Flask extensions include:

- Database: `Flask-SQLAlchemy`_
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
to use it with `Flask-SQLAlchemy`_.

.. _a la NPR: http://blog.apps.npr.org/2014/07/29/everything-our-app-template-does.html

Interpretations
===============

Software development is a trade driven by best practices that form over time.
Decisions should be made by people who understand the in's and out's of their
product or service's needs.

Flask is pure, but you'll always be missing something
-----------------------------------------------------

The one thing that strikes me about Flask is it's really meant to stay out
of your way. The API is, much like this website, documented in sphinx,
it's straight-forward and puts code first.

I feel it almost puts the the job of getting a product shipped secondary.
It's *too* utilitarian, *too* much of a swiss-army knife.

Over 10 years, the web hasn't changed that fundamentally that Rails and
Django broke. On the contrary, they thrived since at the end of the day,
you're just serving up JSON, HTML, CSS and JS assets. Flask will get you
that far.

What about authentication?

Well you have no way to store the users. So you grab SQLAlchemy, peewee,
or MongoEngine. There's your database back-end.

Now you have to build your own user schema. Do you want to use email's as
username? What about your password hashing? Maybe Flask-Security or
Flask-Login will do here. OK, fair enough.

Meanwhile, `Django would have
<https://docs.djangoproject.com/en/1.11/topics/auth/default/>`_ the ORM, User
Model, authentication decorators for views, *and* :class:`login forms <django:django.contrib.auth.views.LoginView>`,
with database-backed validation. And it's pluggable and templated.

OK, what about JSON and REST?

Well if it involves a database backend, you have to cover that.

Here's where is gets hairy. You don't really have a *de facto* python
object for database results, like Django's ``QuerySet``. So, you're not
going to have easy database backed validations in PUT and POST.

If you don't have an authentication system, it's also trickier to create
an OAuth like token system to grant time-block'd permissions to slices of
your data you want to make available. Stuff I'd get for free with
`django-rest-framework's django-guardian integration
<http://www.django-rest-framework.org/api-guide/permissions/#djangoobjectpermissions>`_,
in many cases aren't covered by the contrib community at all, and you're left to
StackOverflow, aka programming your own solution. Taking time away from you.

It's also rather error-prone to program your own replacements to these
things. You don't have the benefit over thousands of others relying on the
library in production to report back if there's unexpected behavior. The
refinment from it being around for years. You'll have those customer-losing bugs
where something breaks and it isn't until months later you get that `Intercom`_
message that something's broke.

.. _Intercom: https://www.intercom.com/

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

So we've covered Flask and Django, their philosophies, their API's,
juxtaposed against how it worked for me in practice. Some links to
specific API's across a few python libraries, documentation sections, and
project homepages should prove fruitful in this being a resource you can
come back to.

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

Bonus: Cookiecutter template for Flask projects
-----------------------------------------------

Since I still use Flask. I maintain a `cookiecutter <https://cookiecutter.readthedocs.io>`_
`template project for it <https://github.com/tony/cookiecutter-flask-pythonic>`_.
Feel free to use it as a sample project. In terminal:

.. code-block:: sh

   pip install --user cookiecutter
   cookiecutter https://github.com/tony/cookiecutter-flask-pythonic.git
   cd ./path-to-project
   virtualenv .env && . .env/bin/activate
   pip install -r requirements.txt
   ./manage.py

Bonus: How do I learn Django or Flask?
--------------------------------------

Preparation:

- Understand how python `virtual environments`_ (see `Real Python
  <https://realpython.com/blog/python/python-virtual-environments-a-primer/>`_'s
  tutorial) and PATH's work. This is an absolute must. Also, check out my
  book *The Tao of tmux* `available online free
  <https://leanpub.com/the-tao-of-tmux/read>`_ for some good coverage of
  the terminal.
- Grab `Django's documentation PDF
  <https://media.readthedocs.org/pdf/django/latest/django.pdf>`_ and `Flask's
  documentation PDF <http://flask.pocoo.org/docs/dev/.latex/Flask.pdf>`_. Read
  it on a smart phone or keep it open in a PDF reader.
- In your spare time, get in the habit of reading python docs on
  ReadTheDocs.org (a documentation hosting website)

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

