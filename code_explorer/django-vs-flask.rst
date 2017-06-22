:orphan:

.. _django-vs-flask:

===============
Django vs Flask
===============
A practitioner's perspective
============================

*June 2017*

This analysis is a comparison of 2 python frameworks, Flask and Django.
It discusses their features and how their technical philosophies impact software
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

Class-based: :doc:`django <django:topics/class-based-views/index>` and
`flask <http://flask.pocoo.org/docs/0.12/api/#class-based-views>`_

Context information
-------------------
  
Passed into HTML template for processing.

:meth:`django:django.template.Template.render` (pass :py:class:`dict` into
:class:`~django:django.template.Context` object)
  
:func:`flask:flask.render_template` (accepts :py:class:`dict`)

HTML template engine
--------------------
  
Renders template via context information.

:doc:`Django's templating <django:ref/templates/index>` and :doc:`Flask's templating <flask:templating>`

Response object
---------------
  
Object with HTTP meta information and content to send to the browser.

:class:`django:django.http.HttpResponse` and :class:`flask:flask.Response`

Static file-handling
--------------------

Handles static files like CSS, JS assets, and downloads.

:doc:`Static files in django <django:howto/static-files/index>` and
`Static files in Flask <http://flask.pocoo.org/docs/0.12/quickstart/#static-files>`_

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

Django's scope
--------------

Django is a framework. The aspects django occupies are:

- mapping :doc:`database schemas <django:topics/db/models>`, :doc:`their queries <django:topics/db/queries>`,
  and :django:ref:`query results <django:retrieving-objects>` to objects
- mapping :doc:`URL patterns <django:topics/http/urls>` to :doc:`views
  <django:topics/http/views>` containing business logic
- providing :doc:`request information <django:ref/request-response>` such as
  GET, PUT, and `session stuff to views <https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-sessions-in-views>`_
  (:class:`~django:django.http.HttpRequest`)
- presenting data, including HTML :doc:`templates <django:topics/templates>` and
  :django:ref:`django:serialization-formats-json` (:class:`~django:django.http.HttpResponse`)
- :doc:`environmental configuration <django:topics/settings>` (settings) and an
  environment variables (:envvar:`DJANGO_SETTINGS_MODULE`) e.g. dev, staging, prod
  workflows
  
A tool kit of libraries that abstract the monotony of common tasks in
web projects.

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

.. admonition:: Code Editors
    :class: seealso
  
    Free tools in the community such as `jedi`_ provide navigation of modules,
    functions and classes to editors like `vim`_, `Visual Studio Code`_ and
    `Atom`_.

:ref:`Python classes <tut-classes>` benefit from many real-world
examples being available in the open source community to study.
They're a pleasure incorporating in your code. An example for django
would be :doc:`class-based views <django:topics/class-based-views/index>`
which shipped in :doc:`Django 1.3 <django:releases/1.3>`.

.. admonition:: OOP + Python
    :class: seealso

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
Django injects the user's request and any URL group pattern matches to
views when the user visits a page matching a URL pattern.

1. :class:`~django:django.http.HttpRequest` is passed into the view as ``request``.

2. Since the URL pattern, ``r'^profile/(?P<pk>\d+)/$'``, contains a named group,
   ``pk``, that will be passed via :ref:`tut-keywordargs` ``**kwargs``.

   If it was ``r'^profile/(\d+)/$'``, it'd be passed in as :func:`tuple`
   argument into the ``*arg`` parameter.
   
   .. admonition:: Arguments and Parameters
       :class: seealso
     
       Learn :ref:`the difference between arguments and parameters
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

If  *profile/1* is missing a template, accessing the page displays an error::
  
    django.template.exceptions.TemplateDoesNotExist: core/myuser_detail.html

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

Next, let's try usernames instead of user ID's, */profile/yourusername*. In the
views file::

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

  - When an :ref:`attribute <tut-classobjects>` of ``django.conf.settings``
    is accessed, it will do a onetime "setup". The section :ref:`djangos-initialization`
    shows there's a few ways settings get configured.
  - *Singleton*, meaning that it can be imported it the application code,
    retrieving the same instance of the object.
    
    .. admonition:: Reminder
       :class: note

       Sometimes global interpreter locks and thread safety are brought up when
       discussing languages. Web admin interfaces and JSON API's aren't CPU
       bound. Most web problems are I/O bound.

       In other words, issues websites face when scaling are concurrency
       related. It's not limited to the dichotomy of concurrency and parallelism.
       Websites scale by offloading to infrastructure such as: `reverse proxies`_,
       task queues (e.g. `Celery`_, `RQ`_), and `Database replication`_.
       Computational heavy backend services are done elsewhere and use different
       tools (kafka, hadoop, spark, Elasticsearch, etc).

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

.. _reverse proxies: https://en.wikipedia.org/wiki/Reverse_proxy
.. _Celery: http://www.celeryproject.org/
.. _RQ: http://python-rq.org/
.. _Database replication: https://en.wikipedia.org/wiki/Replication_(computing)#DATABASE
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

1. Point WSGI server wrapper (e.g. UWSGI) :doc:`to wsgi.py generated by Django <django:howto/deployment/wsgi/index>`
2. uwsgi.py will run `get_wsgi_application() <https://github.com/django/django/blob/1.11.2/django/core/wsgi.py#L5>`_
3. :func:`django:django.setup`
4. Serves WSGI-compatible response

Flask
=====

Flask is also built and maintained in the open source community. The project, as well
as its dependencies, `Jinja2`_ and `Werkzeug`_, are `Pallets projects`_. The creator of
the software itself is Armin Ronacher. Initial release April 1, 2010.

What Flask provides
-------------------

- :doc:`Template system <flask:templating>` via `Jinja2`_
- :ref:`URL routing <flask:url-route-registrations>` via `Werkzeug`_
- Modularity via :ref:`blueprints <flask:blueprints>`
- In-browser REPL-powered tracebook debugging via Werkzeug's
- Static file handling

Extending Flask
---------------

Since Flask doesn't include things like an ORM, authentication and access
control, it's up to the user to include libraries to handle those a la
carte.

Popular Flask extensions include:

- Database: `Flask-SQLAlchemy`_
- REST: `Flask-RESTful`_ (`flask-restful-swagger`_), `Flask API`_
- Admins: `Flask-Admin`_ `Flask-SuperAdmin`_
- Auth: `Flask-Login`_, `Flask-Security`_
- Asset Pipeline: `Flask-Assets`_, `Flask-Webpack`_
- Commands: `Flask-Script`_

.. _Flask-Webpack: https://github.com/nickjj/flask-webpack
.. _Flask-Assets: https://flask-assets.readthedocs.io
.. _Flask-RESTful: https://flask-restful.readthedocs.io/
.. _flask-restful-swagger: https://github.com/rantav/flask-restful-swagger
.. _Flask API: http://www.flaskapi.org/
.. _Flask-Admin: https://github.com/flask-admin/flask-admin
.. _Flask-SuperAdmin: https://github.com/SyrusAkbary/Flask-SuperAdmin
.. _Flask-Login: https://flask-login.readthedocs.io/
.. _flask-security: https://flask-security.readthedocs.io
.. _Flask-SQLAlchemy: http://flask-sqlalchemy.pocoo.org/
.. _Flask-Script: https://flask-script.readthedocs.io/

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

.. _configuring-flask:

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

.. admonition:: Tangent: Confusion with configs
   :class: note

   Despite the pythonic use of :meth:`~flask:flask.Config.from_object` and the
   :ref:`pattern of building classes <config-dev-prod>` to point to classes
   for dev/prod setups in official documentation`, and the abundance of
   string to python object importation utilities, it doesn't point to a class.

   There's a potential `Chesterton's Fence <https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence>`_
   issue also. I `made an issue <https://github.com/pallets/flask/issues/2368>`_ about it
   to document my observations. The `maintainer's response <https://github.com/pallets/flask/issues/2368#issuecomment-308116267>`_
   was they're enhancing the :envvar:`FLASK_APP` environmental variable
   to `specify an application factory with arbitrary arguments
   <https://github.com/pallets/flask/blob/b5f4c52/CHANGES#L46>`_.)

   In the writer's opinion, an API-centric framework like flask introducing
   the ``FLASK_APP`` variable exacerbates the aforementioned confusion. Why add
   ``FLASK_APP`` when :meth:`~flask:flask.Config.from_envvar` is available? Why
   not allow `pointing to a config object and leveraging what flask already has
   and exemplifies in its documentation <https://en.wikipedia.org/wiki/Principle_of_least_astonishment>`_?

   It's already de facto in the flask community to point to modules and
   classes when apps bootstrap. There's a reason for that. Maintainer's
   should harken back on using the tools and gears that originally earned flask
   its respect. In microframeworks, nonorthogonality sticks out like a sore
   thumb.

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

Flask's initiation is different then Django's.

Before any server is started, the :class:`~flask:flask.Flask` object
must be initialized. The ``Flask`` object acts a registry URL mappings, view
callback code (business logic), hooks, and other configuration data.

The ``Flask`` object only requires one argument to initialize, the
so-called ``import_name`` parameter. This is used as a way to identify
what belongs to your application. For more information on this parameter,
see *About the First Parameter* on the :ref:`Flask API documentation page
<flask:api>`::

    from flask import Flask
    app = Flask('myappname')

Above: ``app``, an instantiated ``Flask`` object. No server or
configuration present (yet).

.. _flask_object:

Dissecting the ``Flask`` object
"""""""""""""""""""""""""""""""

During the initialization, the ``Flask`` object hollowed out :py:class:`dict`
and :py:class:`list` attributes to store "hook" functions, such as:

- :attr:`~flask:flask.Flask.error_handler_spec`
- :attr:`~flask:flask.Flask.url_build_error_handlers`
- :attr:`~flask:flask.Flask.before_request_funcs`
- :attr:`~flask:flask.Flask.before_first_request_funcs`
- :attr:`~flask:flask.Flask.after_request_funcs`
- :attr:`~flask:flask.Flask.teardown_request_funcs`
- :attr:`~flask:flask.Flask.url_value_preprocessors`
- :attr:`~flask:flask.Flask.url_default_functions`
- :attr:`~flask:flask.Flask.template_context_processors`
- :attr:`~flask:flask.Flask.shell_context_processors`

See a pattern above? They're all function callbacks that are triggered
upon events occuring. ``template_context_processors`` seems a lot like
Django's :ref:`context processor <django:subclassing-context-requestcontext>`
middleware.

- :attr:`~flask:flask.Flask.blueprints`: blueprints
- :attr:`~flask:flask.Flask.extensions`: extensions
- :attr:`~flask:flask.Flask.url_map`: url mappings
- :attr:`~flask:flask.Flask.view_functions`: view callbacks

So why list these? Situational awareness is a key matter when using a micro
framework. Understanding what happens under the hood ensures confidence the
application is handled by the developer, not the other way around.

Hooking in views
""""""""""""""""

The application object is instantiated relatively early because it's
used to decorate views.

Still, at this point, you don't have a server running yet. Just a
``Flask`` object. Most examples will show the object instantiated as
``app``, you can of course use any name.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World'

The :meth:`flask:flask.Flask.route` decorator is just a fancy way of doing
:meth:`flask:flask.Flask.add_url_rule`::

    from flask import Flask
    app = Flask(__name__)

    def hello_world():
        return 'Hello, World'
    app.add_url_rule('/', 'hello_world', hello_world)

Configure the Flask object
""""""""""""""""""""""""""

.. seealso::

    :ref:`configuring-flask`

Here's an interesting one: Generally configuration isn't added until after
the *after* initializing the Python object.

You could make a function to act as a factory/bootstrapper for flask
objects. There's nothing magical here, nothing's tying you down - it's
python. Unlike with django, which controls initialization, a Flask project
has to handle minutiae of initialization on its own.

In this situation, let's wrap it in a pure function:

.. code-block:: python

    from flask import Flask

    class DevConfig(object):
        DEBUG = True
        TESTING = True
        DATABASE_URL = 'sqlite://:memory:'

    def get_app():
        app = Flask(__name__)
        app.config.from_object(DevConfig)
        return app

Start Flask web server
""""""""""""""""""""""

.. code-block:: python

    if __name__ == '__main__':
        app = get_app()
        app.run()

See :meth:`flask:flask.Flask.run`.

.. versionadded:: 0.12

    Flask also has a :ref:`command-line API <flask:cli>`

Flask and Databases
-------------------

Unlike Django, Flask doesn't tie project's to a database.

There's no rules saying a Flask app has to connect to a database. It's
python, flask could used to make a proxy/abstraction of a thirdparty REST API.
Or a quick web front-end to a pure-python program. Another possiblity,
generating a purely static website with no SQL backend `a la NPR`_.

If a website is using RDBMS, which is often true, a popular choice is
SQLAlchemy. `Flask-SQLAlchemy`_ helps assist in gluing them together.

SQLAlchemy is mature (a decade older than this writing), battle-tested
with a massive test suite, dialects for many SQL solutions. It also
provides something called ":ref:`core <sqlalchemy:core_toplevel>`" underneath the hood that allows building
SQL queries via python objects.

SQLAlchemy is also active. Innovation keeps happening. The change log
keeps showing good things happening. Like Django's ORM, SQLAlchemy's
documentation is top notch. Not to mention, `Alembic`_, a project by the same
author, harnesses SQLAlchemy to power migrations.

.. _Alembic: http://alembic.zzzcomputing.com/

.. _a la NPR: http://blog.apps.npr.org/2014/07/29/everything-our-app-template-does.html

Interpretations
===============

Software development best practices form over time. Decisions should be made by
those with familiarity with their product or service's needs.

Over the last 10 years, the fundamentals of web projects haven't shifted.
None of Rails' or Django's MVC workflows were thrown out the window. On the
contrary, they thrived. At the end of the day, the basics still boils down to
JSON, HTML templates, CSS, and JS assets.

Flask is pure, easy to master, but can lend to reinventing the wheel
--------------------------------------------------------------------

Flask is meant to stay out of the way and put the developer into control.
Even over things as granular as piecing together the ``Flask`` object,
registering blueprints and starting the web server.

The API is, much like this website, is documented using `sphinx`_. The reference
will become a goto. To add to it, a smaller codebase means a developer can
realistically wrap their brain around the internals.

Developers who that find implicit behavior to be a hindrance and thrive in
explicitness will feel comfortable using Flask.

However, this comes at the cost of omitting niceties many web projects would
actually *find helpful*, not an encumbrance. It'll also leave developer's
relying on third party extensions. To think of a few that'd come up for
many:

What about authentication?

There's no way to store the users. So grab SQLAlchemy, peewee, or MongoEngine.
There's the database back-end.

Now to building the user schema. Should the website accept email addresses as
usernames? What about password hashing? Maybe `Flask-Security`_ or
`Flask-Login`_ will do here.

Meanwhile, `Django would have
<https://docs.djangoproject.com/en/1.11/topics/auth/default/>`_ the ORM, User
Model, authentication decorators for views, *and* :class:`login forms <django:django.contrib.auth.views.LoginView>`,
with database-backed validation. And it's pluggable and templated.

What about JSON and REST?

If it involves a database backend, that still has to be done (like above).
To help Flask projects along, there are solutions like `Flask API`_ (inspired by
Django Rest Framework) and `Flask-RESTful`_.

Flask's extension community chugs, while Django's synergy seems unstoppable
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

That isn't to say Flask has no extension community. It does. But it lacks
the cohesion and comprehensiveness of Django's. Even in cases where
there are extensions, there will be corner cases where features are just
missing.

For instance, without an authentical and permissions system, it's difficult to
create an OAuth token system to grant time-block'd permissions to slices of
data to make available. Stuff available for free with
`django-rest-framework's django-guardian integration
<http://www.django-rest-framework.org/api-guide/permissions/#djangoobjectpermissions>`_,
which benefit from both Django's ORM and its permission system, in many cases
aren't covered by the contrib community at all. This is dicussed in
greater detail in :ref:`open-source-momentum`.

.. _Intercom: https://www.intercom.com/

Django is comprehensive, solid, active, customizable, and robust
----------------------------------------------------------------

:django:ref:`Batteries included <tut-batteries-included>`.

A deep notion of customizability and using subclassed Field, Forms, Class
Based Views, and so on to suit situations.

The components django provided complement each other.

Rather than dragging in hard-requirements, nothing forces you to:

- use the Form framework
- if using the Form framework, to:

  - back forms with models (ModelForm)
  - output the form via :meth:`~django:django.forms.Form.as_p`,
    :meth:`~django:django.forms.Form.as_table`, or
    :meth:`~django:django.forms.Form.as_ul`
- use class-based views
- use a *specific* class-based view
- if using a class-based view, fully implement every method of a specialized-view
- use django's builtin User model

Above are just a few examples, but Django doesn't strap projects into using
every battery.

That said, the :class:`~django:django.db.models.query.QuerySet` object
plays a huge role in catalyzing the momentum django provides. It provides
easy database-backed form validations, simple object retrieval with views,
and code readability. It's even utilized downstream by extensions like
django-filters and django-tables2. These two plugins don't even know about
each other, but since they both operate using the same database object,
you can use django-filter's filter options to facet and search results
that are produced by django-tables2.

.. _open-source-momentum:

Open source momentum
--------------------

Flask, as a microframework, is relatively dormant from a feature
standpoint. Its scope is well-defined.

Flask isn't getting bloated. Recent pull requests seem to be on tweaking and
refining facilities that are already present.

It's not about stars, or commits, or contributor count. It's about features and
support niceties that can be articulated in `change logs <https://github.com/pallets/flask/blob/master/CHANGES>`_.

Even then though, it's hard to put things into proportion. Flask includes
`Werkzeug`_ and `Jinja2`_ as hard dependencies. They run as independent
projects (*i.e. their own issue trackers*), under the `pallets
organization <https://github.com/pallets>`_.

Django wants to handle everything on the web backend. Everything fits
together. And it needs to, because it's a framework. Or a framework
of frameworks. Since it covers so much ground, let's try once again
to put it into proportion, against Flask:

============================== ================================================
Django                         Flask
============================== ================================================
Django ORM                     SQLAlchemy, MongoEngine
Django Migrations              Alembic
Django Templates               Jinja2
Django Core / URL's            Werkzeug
Django Forms  (ModelForm)      WTForms (`WTForms-Alchemy`_)
Django Commands                Flask-Script (flask bundles :ref:`CLI support 
                               <flask:cli>` as of 0.11)
============================== ================================================

.. _WTForms-Alchemy: https://wtforms-alchemy.readthedocs.io/

There are also feature requests that come in, often driven by need of the
web development community, and things that otherwise wouldn't be
considered for Flask or Flask extension. Which kind of hurts open source,
because there's code that could be reuseable being written, but not worth
the effort to make an extension for. So there are `snippets
<http://flask.pocoo.org/snippets/>`_ for that.

And in a language like Python where packages, modules, and duck typing rule,
I feel snippets, while laudable, are doomed to fall short in keeping in
check perpetually recreating patterns someone else done. Not to mention,
snippets don't have CI, nor versioning, nor issue trackers (maybe a comment
thread).

By not having a united front, the oppurtunity for synergetic efforts that bridge
across extensions (a la Django ORM, Alchemy, DRF, and django-guardian) 
fail to materialize, creating extensions that are porous. This leaves devs to
fill in the blanks for all-inclusive functionality that'd already be
working had they just picked a different tool for the job.

Conclusion
==========

We've covered Flask and Django, their philosophies, their API's,
and juxtaposed those against the writer's personal experiences in production and
open source. The article included links to specific API's across a few python
libraries, documentation sections, and project homepages. Together, they should
prove fruitful in this being a resource to come back to.

Flask is great for a quick web app, particularly for a python script to build a
web front-end for.

If already using SQLAlchemy models, it's possible to get them working with
a Flask application with little work. With Flask, things feel in control.

However, once relational databases come into play, Flask enters a cycle of
diminishing returns. Before long, projects will be dealing with forms, REST
endpoints and other things that are all best represented via a declarative model
with types. The exact stance :doc:`Django's applications <django:ref/applications>`
take from the beginning.

There's an informal perception that :django:ref:`Batteries included <tut-batteries-included>`
may mean a growing list of ill-maintained API's that get hooked into every
request. In the case of Django, everything works across the board. When an
internal Django API changes, Django's testsuites to break and the appropriate
changes are made. So stuff integrates. This is something that's harder to do 
when there's a lot of packages from different authors who have to wait for
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

Preparation
"""""""""""

- Understand how python `virtual environments`_ and `PATH`_'s work:
  
  - `Real Python's tutorial on virtualenvs 
    <https://realpython.com/blog/python/python-virtual-environments-a-primer/>`_.
  - Check out my book *The Tao of tmux* `available online free
    <https://leanpub.com/the-tao-of-tmux/read>`_ for some good coverage of
    the terminal.
- For learning python, here are some free books:

  - `Learn Python the Hard Way <https://learnpythonthehardway.org/book/>`_
  - `The Hitchhiker's Guide to Python <https://python-guide.readthedocs.io/>`_
- Grab `Django's documentation PDF
  <https://media.readthedocs.org/pdf/django/latest/django.pdf>`_ and `Flask's
  documentation PDF <http://flask.pocoo.org/docs/dev/.latex/Flask.pdf>`_. Read
  it on a smart phone or keep it open in a PDF reader.
- Get in the habit of reading python docs on `ReadTheDocs.org`_, a documentation
  hosting website.

.. _PATH: https://en.wikipedia.org/wiki/PATH_(variable)
.. _ReadTheDocs.org: https://www.readthedocs.org

Developing
""""""""""

- Make a hobby website in django or flask.
  
  Services like `Heroku`_ are free to try, and simple to deploy Django
  websites to.

  For more free hosting options see https://github.com/ripienaar/free-for-dev.
  
  DigitalOcean plans `start at $5/mo <https://m.do.co/c/a8d3c8586c91>`_
  per instance. Supports FreeBSD with ZFS.
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

Future articles
===============

I'm considering creating some articles or books that go deeper into Python
internals.

- Django's ORM
- Django's startup
- Flask's internals / code overview
- Django's internals / code overview
- Numpy, Pandas internals
- CPython internals
- Pypy internals

Talking through the code and patterns in large-scale applications is a good way
to teach others. In lieu of that, they're fun to read. If you have a request,
send an email, tony @ git-pull.com

Hire me
=======

Looking to hire a Flask or Django developer remote? Teacher? Send me an email, tony
at git-pull.com.

Like my stuff? :ref:`Your support is appreciated! <support>`

.. _Sphinx: http://sphinx-doc.org
.. _Pallets projects: https://www.palletsprojects.com/
.. _Jinja2: http://jinja.pocoo.org/
.. _Werkzeug: http://werkzeug.pocoo.org/
