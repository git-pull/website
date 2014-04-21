.. _reST, docutils, sphinx, readthedocs:

#########################
reST, docutils and sphinx
#########################

Journeying through reST, docutils, sphinx and extensions.

For those designing themes based upon reStructuredText, docutils, sphinx or any of its dependencies, I'd like to save your time by clearing the fog of ambiguity and seeing the big picture.

Purpose: readthedocs > sphinx > extensions > docutils > reST play a major role in the web. This includes websites, documention and more. It's difficult to have a concrete perception of what is what without diving into the source and researching.

I will begin with an overview at the of reStructuredText, docutils, then sphinx and its extensions.

================
reStructuredText
================

**reStructuredText** sometimes seen as **reST** and **rst**, is a
specification for marking up documents.

*Markup Language* (`Docutil's website about reStructuredText`_) - "reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system." [#]_ It is abbreviated as ``reST``, with an extension of ``.rst``.

Like `Markdown`_, the markup language used on sites like `GitHub`_. `See other document markup languages`_.

reST of course does not translate itself into HTML. It requires a software to do it, I will speak about **Docutils**.

.. [#] http://docutils.sourceforge.net/rst.html

========
Docutils
========

*Processor* - `Docutils Homepage`_ - Docutils is a processor for reST
documents.

Docutils is used as a library by python projects for websites, books and as a component of larger documentation software.

The reST markup is parsed into a tree of nodes (computer speak) but eventually a `writer`_.

One of the writers we use is ``html4css1``. 

The output of any ``docutils.writer``, especially ``html4css1`` can be customized by 1. overriding stylesheets 2. subclassing.

1. **Overriding stylesheets** can be see at http://docutils.sourceforge.net/docs/howto/html-stylesheets.html.a At least design to the rules of `html4css1.css`_ or customize upon that.

2. **Subclassing** can be seen in `Github's reST parser`_. ``docutils.writers.html4css1`` is a writer for outputting reST to html. This may require needing to custom `html4css1.css`_.

To see examples of docutils used in real software projects, check out `Docutils in the wild / use cases`_, such as `PEP website and docutils`_ and `Github's reST parser`_.

Theming Docutils
----------------

In practice, most HTML output by plain reST is going to be the same. This is thanks to docutils using a consistently boring HTML writer, which promises you, at the core, you will be seeing the same HTML and classes... at this level.

Internally, 99% of cases, Docutils uses generates HTML via the same plugin (``html4css1``) leaving much of the core HTML, classes and etc. consistent.

**at this level?** Seldom will be you interfacing with docutils by itself / in the raw.

- You will exceptions to this, for one, cases like `Github's reST parser`_, a few customizations are made to the output of standard ReST. The example: the default writer outputs ``<table>``'s tables ``border=1`` [#]_, so `reST files on GitHub preview with a black border`_. The odnly way fix this was to `override standard HTML output`_.
- `Sphinx`_ greatly builds upon docutils by added new default roles, directives (reST and docutils is extendable). See more there.

.. [#] http://sourceforge.net/p/docutils/code/7661/tree/trunk/docutils/docutils/writers/html4css1/__init__.py#l1556
.. _writer: http://repo.or.cz/w/docutils.git/tree/HEAD:/docutils/docutils/writer
.. _override standard HTML output: https://github.com/github/markup/pull/220/files
.. _reST files on GitHub preview with a black border: https://github.com/github/markup/pull/220

======
Sphinx
======

*Documentation Generator* (`Sphinx Homepage`_) **Sphinx** is used to build Documentation projects. If docutils is a machine, sphinx is the factory. One of many `documentation generators`_.

Sphinx has a theming system, supports extensions, and an assembly line that allows docutils to "hook" in at various points during the build process.

Sphinx implements concepts in `Docutils`_ such as roles and directives in its own way. It introduces them in its own Extension system. Sphinx extensions can hook into python projects at various times providing everything from sweeping facelifts to meticulously OCD-driven tweaks.

Here are some **sphinx projects** and their corresponding HTML and PDF versions.

*todo* flask, python 2.7, python 3, sqlalchemy, non python projects

Theming Sphinx
--------------

**Note:** This builds upon teming in `Theming Docutils`_, as sphinx builds upon `Docutils`_ as a component.

You are building a `theme for sphinx`_, keep in mind:

1. Theme *at least* the `html4css1.css`_ rules or accept the defaults.

   Leaving anything missed here **will** cause standard reST to show up incorrectly :(.

2. Theme *at least* the `basic.css_t`_ rules or accept the defaults (``@import url("basic.css");``). 

   To build upon the defaults, you can ``@import url("basic.css");`` into your ``.css_t`` file. You can see an example of this at `pyramid.css_t`.

   One weak point of sphinx, if you have viewed the ``basic.css_t`` file, is wtf is going where here.

3. Know the default templates, and override them if you want:

   Here are the default templates. https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a/sphinx/themes/basic?at=default

4. Understand the concept: the "layout" and the "content"

   **The Content:** output of reST markup The CSS and HTML rules for the
   content in docutils and Sphinx are vague, generic and monotonous on
   purpose. Generated HTML output should be the same. This is because the
   innards (the content generated from reST) has no opinions.

   Theming the content output of reST is more akin to `typesetting`_.

   If in doubt, you can inherit defaults from `basic.css_t`_ via ``@import
   url("basic.css");`` in your CSS file and this in theme.conf:

   .. code-block:: ini

       [theme]
       inherit = basic
       stylesheet = yourtheme.css

   or copy-paste sections where parts of your theme look unstyled.

   **The Layout:** The layout is the outer shell of the documentation.
   Inside it, lies the content. Here you are safe to incorporate template
   options / variables `Jinja2`_ style. This is where design comes
   together and things get normal.

   The HTML wrapping the theme, the ``.css_t file``, the sidebars,
   headers, etc. The wireframe being put together.

Options for dynamic / customizable themes: Sphinx uses ``.css_t`` because you can use ``{{ myoption }}`` to let theme variables pass into it.  *to be completed*

.. _pyramid.css_t: https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a95fb2e83c1f485b8f57366c081e4/sphinx/themes/pyramid/static/pyramid.css_t?at=default
.. _basic.css_t: https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a95fb2e83c1f485b8f57366c081e4/sphinx/themes/basic/static/basic.css_t?at=default
.. _theme for sphinx: http://sphinx-doc.org/theming.html
.. _html4css1.css: http://docutils.sourceforge.net/docutils/writers/html4css1/html4css1.css

===============
Readthedocs.org
===============

*Similar: http://pythonhosted.org/*.

`readthedocs`_, aka rtfd / rtd / readthedocs.org is a website for serving documentation for software projects.

It builds and hosts sphinx documentation projects.

Each software project's documentation may have it's own ``.rst`` files, sphinx extensions and sphinx theme.

===================
FAQ and Miscellanea
===================

What's the relation between readthedocs and sphinx / docutils / reST?
---------------------------------------------------------------------

Sphinx uses docutils, docutils uses reST.

Is docutils a "documentation generator"?
----------------------------------------

I would say no. It processes `reST`_. It doesn't have to be documentation.

It's a staple python library and plays a pivotal shape in the python community. Python is open source and product of not only syntax, but a community and a decade plus of work, PEP or not. There wouldn't be python without rst.

Python.org's official documentation uses Sphinx, and therefore docutils. However important docutils is - it's not part of the standard library.

`Docutils is big`_. It's a project that develops at different pace than core python. It can have contributions to it without needing an issue on the official Python project (a PEP) or a patch to the main codebase (`cpython`_).

.. _Docutils is big: http://sourceforge.net/p/docutils/code/HEAD/tree/

Docutils in the wild / use cases
--------------------------------

*Non-readthedocs, non-sphinx implementations of docutils.*

PEP website and docutils
~~~~~~~~~~~~~~~~~~~~~~~~

Note: Research on this has been turned out anomalous from what I expected. Despite the fragmentation of docutils from python, docutils itself has PEP-related code in it's own lib. Everyone downloads this with the install the package for some reason - even though they probably don't care about writing PEPs.

A `Python Enhancement Proposal` (PEP) is not isn't documentation. The `PEP website`_ and the `PEP websites' source`_ is in all affects its own project.

1. It doesn't use sphinx.

I am surprised, ``docutils`` has in its core package PEP related code [2]. This means every time ``docutils`` is installed, custom code relating to python's bureaucratic processes are in our projects too.

.. [2]: http://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/writers/pep_html/
.. [3]: http://hg.python.org/peps/file/63595acfe51d/pep2pyramid.py#l316

 The website has instances where it actually overrides this in cases [3]. This is my first instance of what may be *pythpocrisy*. **TODO**: Find out how this happened. Purity in python maybe be spoken divinely through PEP's, but in practice habits are passed like a meme; through example. python.org is like the great sky castle of the python world, good python projects are like examples of world-class cities, great programmers are great people that set examples of best practice and the role models aspiring coders seek to emulate.

As a new explorer - I was not around to read or see how this came about, but I will search. (see TODO above) But for a holy site like PEP to be contradicting python best practice and a contrib module to be hosting code like that needs to be explained in context.

Github's reST parser
~~~~~~~~~~~~~~~~~~~~

While `Markdown`_ is definitely the most popular "markup to HTML" of its type, `GitHub` supports multiple markup languages with `markup`_.

`/lib/github/commands/rest2html`_. What's that? A reST parser. And github/markup is ruby. This docutils implementation subclasses ``docutils.writers.html4css1`` ``Writer`` and ``HTMLTranslator``.

How does it spit out reST? 

.. code-block:: python

    if __name__ == '__main__':
        sys.stdout.write("%s%s" % (main(), "\n"))
        sys.stdout.flush()


`/lib/github/markup.rb`_ (ruby):

.. code-block:: ruby

    def execute(command, target)
      out = ''
      Open3.popen3(command) do |stdin, stdout, _|
        stdin.puts target
        stdin.close
        out = stdout.read
      end
      out.gsub("\r", '')
      # <snip>
    end

    def command(command, regexp, &block)
      command = command.to_s

      if File.exists?(file = File.dirname(__FILE__) + "/commands/#{command}")
        command = file
      end

      add_markup(regexp) do |content|
        rendered = execute(command, content)
        # <snip>
        rendered
      end
    end

I can't read ruby, but it looks like `/lib/github/commands/`_ is hole-punched for a filename existing and the `rest2html`_ script is sent the ``content`` of the file. The ``stdout.read`` is passed up the shoot.

Important here is `/lib/github/markups.rb`_, where the command ``:rest2html`` is passed in if the regex ``/re?st(\.txt)?/`` is matched in the file name.

.. code-block:: ruby

  command(:rest2html, /re?st(\.txt)?/)

(from `/lib/github/markups.rb#L51`_ line 51.)

GitHub, with the script ``_rest2html``, kind of goes out of there way to make reST happy. Their software for markup is ruby, but for ``rest2html`` to work, their server has to have working python, docutils, and the burden of an open cog running python on their service in the light of day. It looks solid, knock one wood, but to someone in charge of security, adding a new language in this way is just more gray hairs.

.. _/lib/github/markups.rb: https://github.com/github/markup/blob/425f4aa10e53461773a715b4e6681421cd415dfe/lib/github/markups.rb
.. _/lib/github/markups.rb#L51: https://github.com/github/markup/blob/425f4aa10e53461773a715b4e6681421cd415dfe/lib/github/markups.rb#L51

.. _markup: https://github.com/github/markup
.. _/lib/github/commands/: https://github.com/github/markup/blob/master/lib/github/commands/
.. _/lib/github/commands/rest2html: https://github.com/github/markup/blob/master/lib/github/commands/rest2html
.. _rest2html: https://github.com/github/markup/blob/master/lib/github/commands/rest2html
.. _/lib/github/markup.rb: https://github.com/github/markup/blob/master/lib/github/markup.rb#L30

=======
Updates
=======

- 04/21/2014 - Mediawiki / Wikipedia does not use markdown, it uses `wiki markup`_. Thank you for catching this Pere Orga.
- 02/05/2014 - Adjust sections. Fix code formatting.
- 11/20/2013 - Moved to www.git-pull.com
- 11/03/2013 - Created.

.. _Python Enhancement Proposal: http://www.python.org/dev/peps/pep-0001/
.. _PEP website: http://www.python.org/dev/peps/
.. _PEP websites' source: http://hg.python.org/peps/file/tip
.. _Docutil's website about reStructuredText: http://en.wikipedia.org/wiki/ReStructuredText
.. _reST: http://en.wikipedia.org/wiki/ReStructuredText
.. _See other document markup languages: http://en.wikipedia.org/wiki/Comparison_of_document_markup_languages
.. _Documentation generators: http://en.wikipedia.org/wiki/Comparison_of_documentation_generators
.. _Docutils Homepage: http://docutils.sourceforge.net/
.. _Sphinx Homepage: http://sphinx-doc.org/
.. _Markdown: http://en.wikipedia.org/wiki/Markdown
.. _typesetting: http://en.wikipedia.org/wiki/Typesetting
.. _Wikipedia: http://wikipedia.org
.. _readthedocs: https://readthedocs.org/
.. _cpython: http://hg.python.org/cpython/
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _GitHub: https://www.github.com/
.. _html4css1.css: http://docutils.sourceforge.net/docutils/writers/html4css1/html4css1.css
.. _wiki markup: http://en.wikipedia.org/wiki/Wiki_markup

**LICENSE:** http://creativecommons.org/licenses/by-nc-nd/3.0/us/

**Copyright:** Tony Narlock 2013

**Build to Markdown**: ``$ pandoc --from=rst --to=markdown
--output=reStructuredText.md reStructuredText.rst``
