.. _django-vs-flask-2017:

=============================
Django vs Flask: 2017 Edition
=============================
Which is better
===============

This is going to be a real comparison with the gloves off. I have used both
extensively and have want to want to save technical decision makers time.

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
devoted to Flask and SQLAlchemy, due to their documentation and pythonics.

Django
======

Today, Django is built and maintained by the open source community. The initial
release was July 21, 2005, by Lawrence Journal-World.

What django provides
--------------------

- :django:ref:`Template Engine <templates>`

  - Filters
  - Tags
  - Context preprocessor middleware (global, per-request :py:class:`dict` you can pile
    data to for templates)
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

Extending
---------

Django has a vibrant third-party development community. Apps are installed
via appending them to the ``INSTALLED_APPS`` in the settings.

Popular django extensions include:

- REST: Django REST Framework, aka "DRF"
- Permissions: django-guardian
- Asset pipelines: django-compressor, django-webpack
- Debugging, Miscellaneous: django-extensions, django-debug-toolbar

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

Pursuit of JS Holy Grail
""""""""""""""""""""""""

In 2014, I remember wanting to be able to re-use code on the front-end and
back-end. So I opted to pick up Node.js. While I was able to use the same
templates. In search of the "Holy Grail". It turned out, Node.js was a
nightmare for scaling code at the time. When you're reusing behavior, middleware
functions are not a replacement for OOP. Having to wrap everything in promises.
In addition, we were left to our own getting validation on forms and REST
endpoints to work. It all had to be done by hand. After what months of begging,
I finally encouraged the supervisor to let us switch to Django. It rescued us.

(Not knocking node.js, I still use it and since 2014, it's grown a lot)

Pursuit of the Pythonic Holy Grail
""""""""""""""""""""""""""""""""""

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

Once you begin implementing a database backend, however, Flask enters a cycle of
diminishing returns. Before long, you'll be dealing with forms, REST endpoints
and other things that are all best represented via a declarative model with
types. Exactly what a Django Apps builds upon.

I didn't write this with the intention to say "Do whatever you like" and
"Your mileage may vary". Nor did I do it to arouse sentiment by being so
direct. Django saves time, and while it forces some conventions, they're
proportional to what need to do the job. It does a lot of what Flask does,
quite frankly, better.

And if things change. I look forward to it. But it's hard. Despite Flask's
success, it doesn't seem likely development will match Django's. It is
still a mighty, mighty microframework.

Hire me
=======

Looking to hire a Flask or Django developer remote? Send me an email, tony
at git-pull.com.

Like my stuff? :ref:`Your support is appreciated! <support>`

