(rest-docutils-sphinx-readthedocs)=

# reST, docutils and sphinx

Journeying through reST, docutils, sphinx and extensions.

For those designing themes based upon reStructuredText, docutils, sphinx or any of its dependencies,
I'd like to save your time by clearing the fog of ambiguity and seeing the big picture.

Purpose: readthedocs > sphinx > extensions > docutils > reST play a major role in the web. This
includes websites, documentation and more. It's difficult to have a concrete perception of what is
what without diving into the source and researching.

I will begin with an overview at the of reStructuredText, docutils, then sphinx and its extensions.

## reStructuredText

**reStructuredText** sometimes seen as **reST** and **rst**, is a specification for marking up
documents. It was defined in [PEP 287][pep 287].

_Markup Language_ ([Docutil's website about
reStructuredText][docutil's website about restructuredtext]) - "reStructuredText is an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax and parser system." [^id2] It is abbreviated as
`reST`, with an extension of `.rst`.

Like [Markdown][markdown], the markup language used on sites like [GitHub][github]. [See other
document markup languages][see other document markup languages].

reST of course does not translate itself into HTML. It requires a software to do it, I will speak
about **Docutils**.

[^id2]: <http://docutils.sourceforge.net/rst.html>

## Docutils

_Processor_ - [Docutils Homepage][docutils homepage] - Docutils is a processor for reST documents.

Docutils is used as a library by python projects for websites, books and as a component of larger
documentation software.

The reST markup is parsed into a tree of nodes (computer speak) but eventually a [writer][writer].

One of the writers we use is `html4css1`.

The output of any `docutils.writer`, especially `html4css1` can be customized by 1. overriding
stylesheets 2. subclassing.

1. **Overriding stylesheets** can be seen at
   <http://docutils.sourceforge.net/docs/howto/html-stylesheets.html> At least design to the rules
   of [html4css1.css][html4css1.css] or customize upon that.
2. **Subclassing** can be seen in [Github's reST parser](github's rest parser).
   `docutils.writers.html4css1` is a writer for outputting reST to html. This may require needing to
   custom [html4css1.css][html4css1.css].

To see examples of docutils used in real software projects, check out [Docutils in the wild / use
cases](docutils in the wild / use cases), such as [PEP website and docutils](pep website and
docutils) and [Github's reST parser](github's rest parser).

### Theming Docutils

In practice, most HTML output by plain reST is going to be the same. This is thanks to docutils
using a consistently boring HTML writer, which promises you, at the core, you will be seeing the
same HTML and classes... at this level.

Internally, 99% of cases, Docutils uses generates HTML via the same plugin (`html4css1`) leaving
much of the core HTML, classes and etc. consistent.

**at this level?** Seldom will be you interfacing with docutils by itself / in the raw.

- You will exceptions to this, for one, cases like [Github's reST parser](github's rest parser), a
  few customizations are made to the output of standard ReST. The example: the default writer
  outputs `<table>`'s tables `border=1` [^id4], so [reST files on GitHub preview with a black
  border][rest files on github preview with a black border]. The odnly way fix this was to [override
  standard HTML output][override standard html output].
- [Sphinx](sphinx) greatly builds upon docutils by added new default roles, directives (reST and
  docutils is extendable). See more there.

[^id4]:
    <http://sourceforge.net/p/docutils/code/7661/tree/trunk/docutils/docutils/writers/html4css1/__init__.py#l1556>

[writer]: http://repo.or.cz/w/docutils.git/tree/HEAD:/docutils/docutils/writer
[override standard html output]: https://github.com/github/markup/pull/220/files
[rest files on github preview with a black border]: https://github.com/github/markup/pull/220

## Sphinx

_Documentation Generator_ ([Sphinx Homepage][sphinx homepage]) **Sphinx** is used to build
Documentation projects. If docutils is a machine, sphinx is the factory. One of many [documentation
generators][documentation generators].

Sphinx has a theming system, supports extensions, and an assembly line that allows docutils to
"hook" in at various points during the build process.

Sphinx implements concepts in [Docutils](docutils) such as roles and directives in its own way. It
introduces them in its own Extension system. Sphinx extensions can hook into python projects at
various times providing everything from sweeping facelifts to meticulously OCD-driven tweaks.

Here are some **sphinx projects** and their corresponding HTML and PDF versions.

_todo_ flask, python 2.7, python 3, sqlalchemy, non python projects

### Theming Sphinx

**Note:** This builds upon teming in [Theming Docutils](theming docutils), as sphinx builds upon
[Docutils](docutils) as a component.

You are building a [theme for sphinx][theme for sphinx], keep in mind:

1. Theme _at least_ the [html4css1.css][html4css1.css] rules or accept the defaults.

   Leaving anything missed here **will** cause standard reST to show up incorrectly :(.

2. Theme _at least_ the [basic.css_t][basic.css_t] rules or accept the defaults
   (`@import url("basic.css");`).

   To build upon the defaults, you can `@import url("basic.css");` into your `.css_t` file. You can
   see an example of this at {}`pyramid.css_t`.

   One weak point of sphinx, if you have viewed the `basic.css_t` file, is wtf is going where here.

3. Know the default templates, and override them if you want:

   Here are the default templates.
   <https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a/sphinx/themes/basic?at=default>

4. Understand the concept: the "layout" and the "content"

   **The Content:** output of reST markup The CSS and HTML rules for the content in docutils and
   Sphinx are vague, generic and monotonous on purpose. Generated HTML output should be the same.
   This is because the innards (the content generated from reST) has no opinions.

   Theming the content output of reST is more akin to [typesetting][typesetting].

   If in doubt, you can inherit defaults from [basic.css_t][basic.css_t] via
   `@import url("basic.css");` in your CSS file and this in theme.conf:

   ```
   [theme]
   inherit = basic
   stylesheet = yourtheme.css
   ```

   or copy-paste sections where parts of your theme look unstyled.

   **The Layout:** The layout is the outer shell of the documentation. Inside it, lies the content.
   Here you are safe to incorporate template options / variables [Jinja2][jinja2] style. This is
   where design comes together and things get normal.

   The HTML wrapping the theme, the `.css_t file`, the sidebars, headers, etc. The wireframe being
   put together.

Options for dynamic / customizable themes: Sphinx uses `.css_t` because you can use `{{ myoption }}`
to let theme variables pass into it. _to be completed_

[pyramid.css_t]:
  https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a95fb2e83c1f485b8f57366c081e4/sphinx/themes/pyramid/static/pyramid.css_t?at=default
[basic.css_t]:
  https://bitbucket.org/birkenfeld/sphinx/src/e5e3a44d334a95fb2e83c1f485b8f57366c081e4/sphinx/themes/basic/static/basic.css_t?at=default
[theme for sphinx]: http://sphinx-doc.org/theming.html
[html4css1.css]: http://docutils.sourceforge.net/docutils/writers/html4css1/html4css1.css

## Readthedocs.org

_Similar: http://pythonhosted.org/_.

[readthedocs][readthedocs], aka rtfd / rtd / readthedocs.org is a website for serving documentation
for software projects.

It builds and hosts sphinx documentation projects.

Each software project's documentation may have it's own `.rst` files, sphinx extensions and sphinx
theme.

## FAQ and Miscellanea

### What's the relation between readthedocs and sphinx / docutils / reST?

Sphinx uses docutils, docutils uses reST.

### Is docutils a "documentation generator"?

I would say no. It processes [reST][rest]. It doesn't have to be documentation.

It's a staple python library and plays a pivotal shape in the python community. Python is open
source and product of not only syntax, but a community and a decade plus of work, PEP or not. There
wouldn't be python without rst.

Python.org's official documentation uses Sphinx, and therefore docutils. However important docutils
is - it's not part of the standard library.

[Docutils is big][docutils is big]. It's a project that develops at different pace than core python.
It can have contributions to it without needing an issue on the official Python project (a PEP) or a
patch to the main codebase ([cpython][cpython]).

[docutils is big]: http://sourceforge.net/p/docutils/code/HEAD/tree/

### Docutils in the wild / use cases

_Non-readthedocs, non-sphinx implementations of docutils._

#### PEP website and docutils

Note: Research on this has been turned out anomalous from what I expected. Despite the fragmentation
of docutils from python, docutils itself has PEP-related code in it's own lib. Everyone downloads
this with the install the package for some reason - even though they probably don't care about
writing PEPs.

A {}`Python Enhancement Proposal` (PEP) is not isn't documentation. The [PEP website][pep website]
and the [PEP websites' source][pep websites' source] is in all affects its own project.

1. It doesn't use sphinx.

I am surprised, `docutils` has in its core package PEP related code [2]. This means every time
`docutils` is installed, custom code relating to python's bureaucratic processes are in our projects
too.

<!---
[2]: http://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/writers/pep_html/
-->

<!---
[3]: http://hg.python.org/peps/file/63595acfe51d/pep2pyramid.py#l316

The website has instances where it actually overrides this in cases [3]. This is my first instance of what may be *pythpocrisy*. **TODO**: Find out how this happened. Purity in python maybe be spoken divinely through PEP's, but in practice habits are passed like a meme; through example. python.org is like the great sky castle of the python world, good python projects are like examples of world-class cities, great programmers are great people that set examples of best practice and the role models aspiring coders seek to emulate.
-->

As a new explorer - I was not around to read or see how this came about, but I will search. (see
TODO above) But for a holy site like PEP to be contradicting python best practice and a contrib
module to be hosting code like that needs to be explained in context.

#### Github's reST parser

While [Markdown][markdown] is definitely the most popular "markup to HTML" of its type, {}`GitHub`
supports multiple markup languages with [markup][markup].

[/lib/github/commands/rest2html][/lib/github/commands/rest2html]. What's that? A reST parser. And
github/markup is ruby. This docutils implementation subclasses `docutils.writers.html4css1` `Writer`
and `HTMLTranslator`.

How does it spit out reST?

```{code-block} python

if __name__ == '__main__':
    sys.stdout.write("%s%s" % (main(), "\n"))
    sys.stdout.flush()

```

[/lib/github/markup.rb][/lib/github/markup.rb] (ruby):

```{code-block} ruby

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

```

I can't read ruby, but it looks like [/lib/github/commands/][/lib/github/commands/] is hole-punched
for a filename existing and the [rest2html][rest2html] script is sent the `content` of the file. The
`stdout.read` is passed up the shoot.

Important here is [/lib/github/markups.rb][/lib/github/markups.rb], where the command `:rest2html`
is passed in if the regex `/re?st(\.txt)?/` is matched in the file name.

```{code-block} ruby

command(:rest2html, /re?st(\.txt)?/)

```

(from [/lib/github/markups.rb#L51][/lib/github/markups.rb#l51] line 51.)

GitHub, with the script `_rest2html`, kind of goes out of there way to make reST happy. Their
software for markup is ruby, but for `rest2html` to work, their server has to have working python,
docutils, and the burden of an open cog running python on their service in the light of day. It
looks solid, knock one wood, but to someone in charge of security, adding a new language in this way
is just more gray hairs.

[/lib/github/markups.rb]:
  https://github.com/github/markup/blob/425f4aa10e53461773a715b4e6681421cd415dfe/lib/github/markups.rb
[/lib/github/markups.rb#l51]:
  https://github.com/github/markup/blob/425f4aa10e53461773a715b4e6681421cd415dfe/lib/github/markups.rb#L51
[markup]: https://github.com/github/markup
[/lib/github/commands/]: https://github.com/github/markup/blob/master/lib/github/commands/
[/lib/github/commands/rest2html]:
  https://github.com/github/markup/blob/master/lib/github/commands/rest2html
[rest2html]: https://github.com/github/markup/blob/master/lib/github/commands/rest2html
[/lib/github/markup.rb]: https://github.com/github/markup/blob/master/lib/github/markup.rb#L30

## Updates

- 02/09/2015 - Added link to [PEP 287][pep 287].
- 04/21/2014 - Mediawiki / Wikipedia does not use markdown, it uses [wiki markup][wiki markup].
  Thank you for catching this Pere Orga.
- 02/05/2014 - Adjust sections. Fix code formatting.
- 11/20/2013 - Moved to www.git-pull.com
- 11/03/2013 - Created.

[python enhancement proposal]: http://www.python.org/dev/peps/pep-0001/
[pep 287]: https://www.python.org/dev/peps/pep-0287/
[pep website]: http://www.python.org/dev/peps/
[pep websites' source]: http://hg.python.org/peps/file/tip
[docutil's website about restructuredtext]: http://en.wikipedia.org/wiki/ReStructuredText
[rest]: http://en.wikipedia.org/wiki/ReStructuredText
[see other document markup languages]:
  http://en.wikipedia.org/wiki/Comparison_of_document_markup_languages
[documentation generators]: http://en.wikipedia.org/wiki/Comparison_of_documentation_generators
[docutils homepage]: http://docutils.sourceforge.net/
[sphinx homepage]: http://sphinx-doc.org/
[markdown]: http://en.wikipedia.org/wiki/Markdown
[typesetting]: http://en.wikipedia.org/wiki/Typesetting
[wikipedia]: http://wikipedia.org
[readthedocs]: https://readthedocs.org/
[cpython]: http://hg.python.org/cpython/
[jinja2]: http://jinja.pocoo.org/docs/
[github]: https://www.github.com/
[wiki markup]: http://en.wikipedia.org/wiki/Wiki_markup

**LICENSE:** <http://creativecommons.org/licenses/by-nc-nd/3.0/us/>

**Copyright:** Tony Narlock 2013

**Build to Markdown**:
`$ pandoc --from=rst --to=markdown --output=reStructuredText.md reStructuredText.rst`
