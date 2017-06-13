.. _django-vs-flask-2017:

=============================
Django vs Flask: 2017 Edition
=============================
A practitioner's perspective
============================

This subject of this analysis is 2 python frameworks, Flask and Django,
their features, and how their technical philosophies impact software
developers. It is based on my experience using both, as well as time spent
personally admiring both codebases.

Synopsis
========

Django is best suited for RDBMS-backed websites. Flask is good for corner cases
that wouldn't benefit from Django's deep intergration with RDBMS.

When using Flask, it's easy to miss the comforts a full-fledge framework
provides. Django's extension community is more active. Django's ORM is superb.
Flask developers will be forced to reinvent the wheel to catch up for things
that'd be quick wins with Django.

Both excel at prototyping; getting an idea off the ground fast, and
giving chiselling away fine-grain details after. Python makes both a joy to work
with.

Concepts present in both frameworks
===================================

Request object
--------------
  
Information of user's client request to server

:class:`flask:flask.Request` and :class:`django:django.http.HttpRequest`

URL routing
-----------  

Routes HTTP requests (GET, POST, PUT, UPDATE), data payload, and URL path

:doc:`Django's routing <django:topics/http/urls>` and :ref:`Flask's routing <flask:url-route-registrations>`

Views
-----  

Invoked when a request matches URL pattern and receives request object

:doc:`Django's views <django:topics/http/views>` and :ref:`Flask's views <flask:views>`

Class-based: :doc:`django <django:topics/class-based-views/index>` and `flask <http://flask.pocoo.org/docs/0.12/api/#class-based-views>`_

Context information
-------------------
  
Passed into HTML template for processing.

:meth:`django:django.template.Template.render` (pass :py:class:`dict` into :class:`~django:django.template.Context` object)
  
:func:`flask:flask.render_template` (accepts :py:class:`dict`)

HTML template engine
--------------------
  
Renders template via context information.

:doc:`Django's templating <django:ref/templates/index>` and :doc:`Flask's templating <flask:templating>`

Response object
---------------
  
Object with HTTP meta information and content to send to the browser.

:class:`django:django.http.HttpResponse` and :class:`flask:flask.Response`

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
- :doc:`Settings <django:topics/settings>`, configurable via :envvar:`DJANGO_SETTINGS_MODULE`
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

Fear of prefabricated solutions
-------------------------------

There's a well-advised stigma prefabricated solutions don't work in the
long term.

Django is a framework. The aspects django occupies are:

- mapping :doc:`database schemas <django:topics/db/models>`, :doc:`their queries <django:topics/db/queries>`,
  and :django:ref:`query results <django:retrieving-objects>` to objects
- mapping :doc:`URL patterns <django:topics/http/urls>` to :doc:`views
  <django:topics/http/views>` containing business logic
- providing :doc:`request information <django:ref/request-response>` such as
  GET, PUT, and :django:ref:`session stuff to views <django:using-sessions-in-views>`
  (:class:`~django:django.http.HttpRequest`)
- presenting data, including HTML :doc:`templates <django:topics/templates>` and
  :django:ref:`django:serialization-formats-json` (:class:`~django:django.http.HttpResponse`)
- :doc:`environmental configuration <django:topics/settings>` (settings) and an
  environment variables (:envvar:`DJANGO_SETTINGS_MODULE`) e.g. dev, staging, prod
  workflows
  
A tool kit of web abstractions that solve proven, repeated problems in the trade.

If it's difficult to visualize a web app in terms of its database schema and
WordPress or Drupal would suffice, Django may not be the strongest pick for
that.

Where a CMS will automatically provide a web admin to post content, toggle
plugins and settings, and even allow user registration and comments, Django
leaves you building blocks of components you customize to the situation.
Programming is required.

Django's programming language, python, also gives it a big boost.

Django uses classes right
"""""""""""""""""""""""""

While python isn't statically typed, its inheritance hierarchy is very
straight-forward and navigable.

.. seealso::
  
    Free tools in the community such as `jedi`_ provide navigation of modules,
    functions and classes to editors like `vim`_ and `Atom`_.

:python:ref:`Python classes <tut-classes>` benefit from many real-world
examples being available in the open source community to study.
They're a pleasure incorporating in your code. An example for django
would be :doc:`class-based views <django:topics/class-based-views/index>`
which shipped in :doc:`Django 1.3 <django:releases/1.3>`.

.. seealso::

    For those seeking a good example of OOP in Python, in addition to
    class-based views, Django is a sweeping resource. It abstracts out
    HTTP requests and responses, as well as SQL dialects in a class
    hierarchy.

    See my answer on HN for *Ask HN: How often do you use inheritance?*:
    https://news.ycombinator.com/item?id=14329256

Stretching the batteries
""""""""""""""""""""""""

Django isn't preventing custom solutions. It provides a couple of frameworks
which complement each other and handles initializing the frameworks being used
via project's settings. If a project doesn't leverage a component Django
provides, it stays out of the way.

Let's try a few examples of how flexible Django is.

**Scenario 1:** Displaying a user profile on a website.

URL pattern is ``r"^profile/(?P<pk>\d+)/$"``, e.g. */profile/1*

Let's begin by using the simplest view possible, and map directly to a
function, grab the user model via :func:`~django:django.contrib.auth.get_user_model`::

    from django.contrib.auth import get_user_model
    from django.http import HttpResponse

    def user_profile(request, **kwargs):
        User = get_user_model()
        user = User.objects.get(pk=kwargs['pk'])
        html = "<html><body>Full Name: %s.</body></html>" % user.get_full_name()
        return HttpResponse(html)

*urls.py*::

    from django.conf.urls import url
    from .views import user_profile

    urlpatterns = [
      url(r'^profile/(?P<pk>\d+)/$', user_profile),
    ]

So where does the ``request, **kwargs`` in ``user_profile`` come from?
From django. When a user visits a page matching a pattern, it injects the
user's request and any URL group patterns to the view:

1. :class:`~django:django.http.HttpRequest` is passed into the view as ``request``.

2. Since the URL pattern, ``r'^profile/(?P<pk>\d+)/$'``, contains a named group,
   ``pk``, that will be passed via :python:ref:`tut-keywordargs` ``**kwargs``.

   If it was ``r'^profile/(\d+)/$'``, it'd be passed in as :func:`tuple`
   argument into the ``*arg`` parameter.
   
   .. seealso::
     
       Learn :python:ref:`the difference between arguments and parameters
       <faq-argument-vs-parameter>`.

**Bring in a high-level view:**

Django has an opinionated flow and a shortcut for this. By using the named
regular expression group ``pk``, there is a class that will automatically
return an object for that key.

So, it looks like a :class:`~django:django.views.generic.detail.DetailView` is
best suited. We only want to get information on one core object.

Easy enough, :meth:`~django:django.views.generic.detail.SingleObjectMixin.get_object`'s
default behavior grabs the PK::

    from django.contrib.auth import get_user_model
    from django.views.generic.detail import DetailView

    class UserProfile(DetailView):
        model = get_user_model()

*urls.py*::

    from django.conf.urls import url
    from .views import UserProfile

    urlpatterns = [
      url(r'^profile/(?P<pk>\d+)/$', UserProfile.as_view()),
    ]

Append :meth:`~django.views.generic.base.View.as_view` to routes using
class-based views.

If  *profile/1* is accessed and missing a template, something happens like:
*django.template.exceptions.TemplateDoesNotExist: core/myuser_detail.html*.
The file location and name depends on the app name and model name.
Create a new template in the location after :exc:`~django:django.template.TemplateDoesNotExist`
in any of the projects *templates/* directories.

In this circumstance, it needs *core/myuser_detail.html*. Let's use the
app's template directory. So inside *core/templates/core/myuser_detail.html*,
make a file with this HTML:

.. code-block:: html

   <html><body>Full name: {{ object.get_full_name }}</body></html>

Custom template paths can be specified via punching out
:attr:`~django:django.views.generic.base.TemplateResponseMixin.template_name`
in the view.

That works in any descendent of :class:`~django.views.generic.base.TemplateView`
or class mixing in :class:`~django.views.generic.base.TemplateResponseMixin`.

.. note::

    Django doesn't require using :class:`~django:django.views.generic.detail.DetailView`.

    A plain-old :class:`~django.views.generic.base.View` could work. Or
    a :class:`~django.views.generic.base.TemplateView` if there's an HTML
    template.
    
    As seen above, there are :doc:`function views <django:topics/http/views>`.
    
    These creature comforts were put into Django because they represent
    bread and butter cases. It makes additional sense when factoring in
    `REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`_.

**Harder:** Getting the user by a username

Even better, let's make the URL's based off the usernames,
*/profile/yourusername*. In the views file::

    from django.contrib.auth import get_user_model
    from django.http import HttpResponse

    def user_profile(request, **kwargs):
        User = get_user_model()
        user = User.objects.get(username=kwargs['username'])
        html = "<html><body>Full Name: %s.</body></html>" % user.get_full_name()
        return HttpResponse(html)

*urls.py*::

    from django.conf.urls import url
    from .views import user_profile

    urlpatterns = [
      url(r'^profile/(?P<pk>\w+)/$', user_profile),
    ]

Notice how we switched the regex to use ``\w`` for alphanumeric
character and the underscore. Equivalent to ``[a-zA-Z0-9_]``.

For the class-based view, the template stays the same. View has an
addition::

    class UserProfile(DetailView):
        model = get_user_model()
        slug_field = 'username'

*urls.py*::

    urlpatterns = [
      url(r'^profile/(?P<slug>\w+)/$', UserProfile.as_view()),
    ]

Another "shortcut" ``DetailView`` provides; a *slug*. It's derived from
:class:`~django:django.views.generic.detail.SingleObjectMixin`. Since the url
pattern has a named group, i.e. ``(?P<slug>\w+)`` as opposed to ``(\w+)``.

But, let's say the named group "slug" doesn't convey enough meaning. We
want to be accurate to what it is, a *username*::

    urlpatterns = [
      url(r'^profile/(?P<username>\w+)/$', UserProfile.as_view()),
    ]

We can specify a :attr:`~django:django.views.generic.detail.SingleObjectMixin.slug_url_kwarg`::

    class UserProfile(DetailView):
        model = get_user_model()
        slug_field = 'username'
        slug_kw_arg = 'username'

**Make it trickier:** User's logged in profile

If a user is logged in, */profile* should take them to their user page.

So a pattern of ``r"^profile/$"``, in *urls.py*::

    urlpatterns = [
      url(r'^profile/$', UserProfile.as_view()),
    ]

Since there's no way to pull up the user's ID from the URL, we need to pull their
authentication info to get that profile.

Django thought about that. Django can attach the user's information to the
:class:`~django:django.http.HttpRequest` so the view can use it. Via
:attr:`~django:django.http.HttpRequest.user`.

In the project's :doc:`settings <django:topics/settings>`, add
:class:`~django:django.contrib.auth.middleware.AuthenticationMiddleware` to
``MIDDLEWARE``::

    MIDDLEWARE = [
        # ... other middleware
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ]

In the view file, using the same template::

    class UserProfile(DetailView):
        def get_object(self):
            return self.request.user

This overrides :meth:`~django:django.views.generic.detail.SingleObjectMixin.get_object`
to pull the :class:`~django:django.contrib.auth.models.User` right out of the
request.

This page only will work if logged in, so let's use
:func:`~django:django.contrib.auth.decorators.login_required`, in
*urls.py*::

    from django.contrib.auth.decorators import login_required

    urlpatterns = [
      url(r'^profile/$', login_required(UserProfile.as_view())),
    ]

That will assure only logged-in users can view the page. It will also send
the user to a login form which forward them back to the page after login.

Even with high-level reuseable components, there's a lot of versatility
and tweaking oppurtunities. This saves time from hacking up solution for common
cases. Reducing bugs, making code uniform, and freeing up time for the
stuff that will be more specialized.

.. _jedi: http://jedi.readthedocs.io/

Retrofit the batteries
""""""""""""""""""""""

Relying on the django's components, such as views and forms, gives developers
certainty things will behave with certainty. When customizations needs to
happen, it's helpful to see if :ref:`subclassing a widget <django:base-widget-classes>`
or :django:doc:`form field <ref/forms/fields>` would do the trick. This assures the
new custom components gets the validation, form state-awareness, and template output
of the form framework.

.. _configuring-django:

Configuring Django
------------------

Django's :doc:`settings <django:topics/settings>` are stored in a python file.
This means that the Django configuration can include any python code,
including accessing environment variables, importing other modules, checking if
a file exists, lists, tuples, arrays, and dicts.

Django relies on an `environment variable`_, :envvar:`DJANGO_SETTINGS_MODULE`, to
load a module of setting information.

Settings are a `lazily-loaded <https://en.wikipedia.org/wiki/Lazy_initialization>`_
`singleton <https://en.wikipedia.org/wiki/Singleton_pattern>`_ object:

  - When an :ref:`attribute <python:tut-classobjects>` of ``django.conf.settings``
    is accessed, it will do a onetime "setup". The section :ref:`djangos-initialization`
    shows there's a few ways settings get configured.
  - *Singleton*, meaning that it can be imported it the application code,
    retrieving the same instance of the object.
    
    .. note::

       If someone brings up global interpreter locks and thread safety,
       gently ask why a customer control panel or JSON API is bottle-necked
       due to CPU constraints; most web problems are I/O bound.

Django use :func:`~importlib.import_module` to turn a string into a
:ref:`module <tut-modules>`. It's kind of like an ``eval``, but strictly for
importing. `It happens here <https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L110>`_.

It's available as an environmental variable is projects commonly have multiple
settings files. For instance, a base settings file, then other files for
`local, development, staging, and production <https://en.wikipedia.org/wiki/Deployment_environment>`_.
Those 3 will have different database configurations. Production will likely have
heavy caching.

To access settings attributes application-wide, do::

    from django.conf import settings

.. warning::
  
   When developing: if not sourced in a virtual enviroment in a shell, the
   settings module (and probably the django module itself) won't be found.
   
   When deploying: not including site-packages in uwsgi onfiguration, will
   result in a similar error.

   This is the single biggest learning barrier python has. It will be a
   hindrance every step of the way until the concept is internalized.

.. _environment variable: https://en.wikipedia.org/wiki/Environment_variable

.. _djangos-initialization:

Django's intialization
----------------------

Django's initialization is complicated. However, its complexity is
proportional to what's required to do the job.

As seen in :ref:`configuring-django`, the settings are loaded as a side-effect
of accessing the setting object.

In addition to that, django maintains an application registry, :data:`~django:django.apps.apps`,
also a singleton. It's populated via :func:`django:django.setup`.

Finding and loading the settings requires an environmental variable is set.
Django's generated manage.py will set a default one if its unspecified.

via command-line / manage.py (development)
""""""""""""""""""""""""""""""""""""""""""

1. User runs ``./manage.py`` (including arguments, e.g. ``./manage.py
   collectstatic``
2. ``settings`` are `lazily loaded`_ upon import of
   ``execute_from_command_line`` of ``django.core.management``.
   
   `Accessing an attribute`_ of ``settings`` (e.g. ``if settings.configured``)
   implicitly imports the settings module's information.

3. ``execute_from_command_line()`` accepts :py:data:`sys.argv` and
   passes them to initialize `ManagementUtility <https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L133>`_

4. ``ManagementUtility.execute()`` (`source
   <https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L284>`_)
   pulls a settings attribute for the first time, invokes
   :func:`django:django.setup` (populating the app registry)
   
5. ``ManagementUtility.execute()`` directs ``sys.argv`` command to the
   appropriate app functions. A list of commands `are cached <https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L44>`_.
   In addition, these are hard-coded:

   - autocompletion
   - ``runserver``
   - help output (``--help``)
   
   In addition, upon running, commands will run :doc:`system checks
   <django:topics/checks>` (since :doc:`Django 1.7
   <django:releases/1.7>`). Any command inheriting from :class:`~django.core.management.BaseCommand`
   runs checks implicitly. ``./manage.py check`` will run checks explicitly.

.. _Accessing an attribute: https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L51
.. _lazily loaded: https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L201

via WSGI (server)
"""""""""""""""""

1. Point WSGI server wrapper (e.g. UWSGI) :django:ref:`to wsgi.py generated by Django <the-application-object>`
2. uwsgi.py will run `get_wsgi_application() <https://github.com/django/django/blob/1.11.2/django/core/wsgi.py#L5>`_
3. :func:`django:django.setup`
4. Serves WSGI-compatible response

Flask
=====

Like Django, Flask is also built and maintained in the open source
community. The creator of the software itself is Armin Ronacher. Initial
release April 1, 2010.

What Flask provides
-------------------

- :doc:`Template system <flask:templating>` via `jinja2 <http://jinja.pocoo.org/>`_
- :ref:`URL routing <flask:url-route-registrations>` via `Werkzeug <http://werkzeug.pocoo.org/>`_
- Modularity via :ref:`blueprints <flask:blueprints>`

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

Used with flask, but not flask-specific (could be used in normal scripts):

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

Configuration is typically added after :class:`~flask:flask.Flask`
*object* is initialized. No server is running at this point::

    app = Flask(__name__)

After initialization, configuration available via a :py:class:`dict`-like
attribute via the :attr:`Flask.config <flask:flask.Flask.config>`.

Only *uppercase* values are stored in the config.

There are a few ways to set configuration options. :py:meth:`dict.update()`::

    app.config.update(KEYWORD0='value0', KEYWORD1='value1')

For the future examples, let's assume this::

  - website/
    - __init__.py
    - app.py
    - config/
      - __init__.py
      - dev.py

Inside *website/config/dev.py*::

    class DevConfig(object):
        DEBUG = True
        TESTING = True
        DATABASE_URL = 'sqlite://:memory:'
    
Subclassing :class:`flask:flask.Config` and pointing to it via
:meth:`flask:flask.Config.from_object` also works::

    from .config.dev import DevConfig
    app.config.from_object(DevConfig)

Another option with ``from_object()`` is a string of the config object's
location::

    app.config.from_object('website.config.dev.DevConfig')

In addition, it'll work with modules (django's style of storing settings).
For *website/config/dev.py*::

    DEBUG = True
    TESTING = True
    DATABASE_URL = 'sqlite://:memory:'

Then::

    app.config.from_object('website.config.dev')

So, this sounds strange, but as of Flask 1.12, that's all there is
regarding importing classes/modules. The rest is all importing python files.

To import an *object* (module or class) from an environmental
variable, do something like::

    app.config.from_object(os.environ.get('FLASK_MODULE', 'web.conf.default'))

:meth:`flask:flask.Config.from_envvar` is spiritually similar to 
``DJANGO_SETTINGS_MODULE``, but looks can be deceiving.

The environmental variable set points to a file, which is interpreted
like a module.

.. caution::

   Despite the pythonic use of :meth:`~flask:flask.Config.from_object` and the
   :ref:`pattern of building classes <config-dev-prod>` to point to classes
   for dev/prod setups in official documentation`, and the abundance of
   string to python object importation utilities, it doesn't point to a class.

   There's a potential `Chesterton's Fence <https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence>`_
   issue also. I made an issue about it at https://github.com/pallets/flask/issues/2368
   to document my observations.

Assuming *website/config/dev.py*::

    DEBUG = True
    TESTING = True
    DATABASE_URL = 'sqlite://:memory:'

Let's apply a configuration from an environmental variable::

    app.config.from_envvars('FLASK_CONFIG')

:envvar:`FLASK_CONFIG` should map to a python file. Any extension::

    export FLASK_CONFIG=website/config/dev.py

Here's where Flask's configurations aren't so orthogonal. There's also a
:meth:`flask:flask.Config.from_pyfile`::

    app.config.from_pyfile('website/config/dev.py')

Flask's Initialization
----------------------

Since Flask doesn't include database models,

Flask and Databases
-------------------

Unlike Django, Flask doesn't tie project's to a database.

There's no rules saying a Flask app has to connect to a database. It's
python, flask could used to make a proxy/abstraction of a thirdparty REST API.
Or a quick web front-end to a pure-python program.

Another possiblity: generating a purely static website with no SQL backend `a la NPR`_.

If a website is using RDBMS, which is often true, a popular choice is
SQLAlchemy. `Flask-SQLAlchemy`_ helps assist in gluing them together.

.. _a la NPR: http://blog.apps.npr.org/2014/07/29/everything-our-app-template-does.html

Interpretations
===============

Software development is a trade driven by best practices that form over time.
Decisions should be made by people who understand the in's and out's of their
product or service's needs.

Flask is pure, but often missing something
------------------------------------------

The one thing that strikes me about Flask is it's really meant to stay out
of the way. The API is, much like this website, documented in sphinx,
it's straight-forward and puts code first.

I feel it almost puts the the job of getting a product shipped secondary.
It's *too* utilitarian, *too* much of a swiss-army knife.

Over 10 years, the web hasn't changed that fundamentally that Rails and
Django broke. On the contrary, they thrived since at the end of the day,
the project is just serving up JSON, HTML, CSS and JS assets. Flask will get
many that far.

What about authentication?

There's no way to store the users. So grab SQLAlchemy, peewee, or MongoEngine.
There's the database back-end.

Now to building the user schema. Should the website accept email addresses as
usernames? What about password hashing? Maybe Flask-Security or
Flask-Login will do here. OK, fair enough.

Meanwhile, `Django would have
<https://docs.djangoproject.com/en/1.11/topics/auth/default/>`_ the ORM, User
Model, authentication decorators for views, *and* :class:`login forms <django:django.contrib.auth.views.LoginView>`,
with database-backed validation. And it's pluggable and templated.

OK, what about JSON and REST?

Well if it involves a database backend, that still has to be done (like
above).

Here's where is gets hairy. There isn't really have a *de facto* python
object for database results, like Django's :class:`~django:django.db.models.query.QuerySet`.
So, stuff like easy database-backed validations in PUT and POST isn't
covered as well.

Without an authentication system, it's also trickier to create
an OAuth like token system to grant time-block'd permissions to slices of
data to make available. Stuff available for free with
`django-rest-framework's django-guardian integration
<http://www.django-rest-framework.org/api-guide/permissions/#djangoobjectpermissions>`_,
in many cases aren't covered by the contrib community at all. Help relies
on sites like StackOverflow and programming the solution in-house. Time is
going to be spent recreating solutions to problems that are already
available and published, distracting attention.

It's also rather error-prone to program replacements to these
things; Without the benefit over thousands of others relying on the
library in production to report back if there's unexpected behavior; The
refinment from it being around for years. It invites increased cases of
customer-losing bugs where something breaks and it isn't until months later.
When that lone `Intercom`_ message mentions something's broke, and has
been for a while.

.. _Intercom: https://www.intercom.com/

Django is comprehensive, solid, active, customizable, and robust
----------------------------------------------------------------

:django:ref:`Batteries included <tut-batteries-included>`.

A deep notion of customizability and using subclassed Field, Forms, Class
Based Views, and so on to suit situations.

The components django provided complement each other.

From the :class:`~django:django.db.models.query.QuerySet`

Open source momentum
--------------------

Flask, as a microframework, is relatively dormant from an activity
standpoint (after all, it's scope is well-defined). It's not about stars, or
commits, or contributor count. It's about features articulated in `change logs <https://github.com/pallets/flask/blob/master/CHANGES>`_.

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

The idea of having a python script there and being able to not tie in a
whole framework is tempting.

Further, being able to keep data models inert, so python scripts as well
as a web app can both pull them inside, is good programming.

A belief by being so philosophically pure and pythonic, time could be saved in
the "long run". All the great virtues of ``import this``.

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
nightmare for scaling code at the time. For reusable behavior, middleware
functions are not a replacement for OOP. Having to wrap everything in promises.
In addition, we were left to our own getting validation on forms and REST
endpoints to work. It all had to be done by hand. After what months of begging,
I finally encouraged the supervisor to let us switch to Django. It rescued us.

(Not knocking node.js, I still use it and since 2014, it's grown a lot)

Anecdote: Pursuit of the Pythonic Holy Grail
""""""""""""""""""""""""""""""""""""""""""""

The other for me, was Flask and SQLAlchemy. Flask had a super fast
template engine. Straight-forward modularization with blueprints. Works
well with current python code stored away. SQLAlchemy `is in AOSA 
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
project homepages should prove fruitful in this being a resource someone can
come back to.

I think Flask is great for a quick web app, particularly for a python
script to build a web front-end for. 

If already using SQLAlchemy models, it's possible to get them working with
a Flask application with little work. With Flask, things feel in control.

Once implementing a database backend, however, Flask enters a cycle of
diminishing returns. Before long, projects will be dealing with forms, REST
endpoints and other things that are all best represented via a declarative model
with types. Which is kind of the philosophy Django's Apps do from the
start.

There's an information perception that batteries included may mean a growing
list of ill-maintained API's that get hooked into every request. In the
case of Django, everything works across the board. When an internal Django
API changes, Django's testsuites to break and the appropriate changes are
made. So stuff integrates. This is something that's harder to do when
there's a lot of packages from different authors who have to wait for
fixes to be released in Flask's ecosystem.

And if things change. I look forward to it. Despite Flask's success, and missing
out on Django's synergy, it is still a mighty, mighty microframework.

Bonus: Cookiecutter template for Flask projects
-----------------------------------------------

Since I still use Flask. I maintain a `cookiecutter <https://cookiecutter.readthedocs.io>`_
`template project for it <https://github.com/tony/cookiecutter-flask-pythonic>`_.

This cookiecutter project will create a core application object that can
load Flask blueprints via a declarative YAML or JSON configuration.

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
- During spare time, get in the habit of reading python docs on
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

