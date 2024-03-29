# News

- _March 2024_

  - {ref}`libtmux <libtmux:index>` refactoring continues

    - [v0.33.0](https://libtmux.git-pull.com/history.html#libtmux-0-33-0-2024-03-17) ([diff](https://github.com/tmux-python/libtmux/compare/v0.32.0...v0.33.0#files_bucket)): Improved new session creation and window splitting.
    - [v0.34.0](https://libtmux.git-pull.com/history.html#libtmux-0-34-0-2024-03-17)-[v0.35.0](https://libtmux.git-pull.com/history.html#libtmux-0-35-0-2024-03-17) ([diff](https://github.com/tmux-python/libtmux/compare/v0.33.0...v0.35.0#files_bucket)): Improved `.cmd()` in respect to targets.

  - Automated fixes via ruff

    Machine-made refactors rendering consistent, tight python code:

    - {ref}`unihan-etl <libtmux:index>`: [v0.34.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-34-0-2024-03-24) ([diff](https://github.com/cihai/unihan-etl/compare/v0.33.1...v0.34.0#files_bucket))
    - {ref}`libvcs <libvcs:index>`: [v0.29.0](https://libvcs.git-pull.com/history.html#libvcs-0-29-0-2024-03-24) ([diff](https://github.com/vcs-python/libvcs/compare/v0.28.2...v0.29.0#files_bucket))
    - {ref}`vcspull <vcspull:index>`: [v1.30.0](https://vcspull.git-pull.com/history.html#vcspull-v1-30-0-2024-03-24) ([diff](https://github.com/vcs-python/vcspull/compare/v1.29.0...v1.30.0#files_bucket))
    - {ref}`libtmux <libtmux:index>`: [v0.36.0](https://libtmux.git-pull.com/history.html#libtmux-0-36-0-2024-03-24) ([diff](https://github.com/tmux-python/libtmux/compare/v0.35.0...v0.36.0#files_bucket))
    - {ref}`tmuxp <tmuxp:index>`: [v1.45.0](https://tmuxp.git-pull.com/history.html#tmuxp-1-45-0-2024-03-24) ([diff](https://github.com/tmux-python/tmuxp/compare/v1.44.0...v1.45.0#files_bucket))

- _February 2024_: Busman's holiday

  - {ref}`libtmux <libtmux:index>`: [v0.31.0](https://libtmux.git-pull.com/history.html#libtmux-0-31-0-2024-02-17) ([diff](https://github.com/tmux-python/libtmux/compare/v0.26.0...v0.31.0post0#files_bucket))

    - API streamlining: e.g. `Pane.select_pane()` -> `Pane.select()`
    - Up next: Options and hooks:
      [libtmux#516](https://github.com/tmux-python/libtmux/pull/516)

  - [CV]\: Add timeline to pull requests

  - {ref}`unihan-etl <unihan-etl:index>`:

    - [v0.31.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-31-0-2024-02-04) ([diff](https://github.com/cihai/unihan-etl/compare/v0.30.0...v0.31.0#files_bucket)): Support updated from UNIHAN [11.0.0](https://www.unicode.org/reports/tr38/tr38-25.html) (May 2018) to [15.1.0](https://www.unicode.org/reports/tr38/tr38-35.html) (Sept 2023), via [unihan-etl#309](https://github.com/cihai/unihan-etl/pull/309/files).
    - [v0.32.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-32-0-2024-02-05) ([diff](https://github.com/cihai/unihan-etl/compare/v0.31.0...v0.32.0#files_bucket)): Highlight examples on the front page: [unihan-etl#253](https://github.com/cihai/unihan-etl/pull/253/files), [unihan-etl#314](https://github.com/cihai/unihan-etl/pull/314/files).
    - [v0.33.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-33-0-2024-02-09) ([diff](https://github.com/cihai/unihan-etl/compare/v0.30.0...v0.33.0#files_bucket)): Lint improvements, fix CSV highlighting.

- _January 2024_:

  - [CV]: Move to tailwind ([cv#1674](https://github.com/tony/cv/pull/1674),
    [diff](https://github.com/tony/cv/pull/1674/files))

- _December 2023_:

  - Moved my [CV] and [social-embed] project to ~~[oxlint]~~ [biome], a [Rust]-based ~~linter~~ linter and formatter:

    - [CV]\: ~~[cv#1667](https://github.com/tony/cv/pull/1667) ([diff](https://github.com/tony/cv/pull/1667/files))~~ [cv#1668](https://github.com/tony/cv/pull/1668) ([diff](https://github.com/tony/cv/pull/1668/files))

    - [social-embed]\: ~~[social-embed#26](https://github.com/social-embed/social-embed/pull/26) ([diff](https://github.com/social-embed/social-embed/pull/26/files))~~ [social-embed#27](https://github.com/social-embed/social-embed/pull/27) ([diff](https://github.com/social-embed/social-embed/pull/27/files))

    [CV]: https://cv.git-pull.com
    [social-embed]: https://social-embed.git-pull.com
    [oxlint]: https://oxc-project.github.io/blog/2023-12-12-announcing-oxlint.html
    [Rust]: https://www.rust-lang.org/
    [biome]: https://biomejs.dev/

  - Documented even more projects w/ [ruff]'s [pydocstyle] linter:

    - {ref}`cihai <cihai:index>`: [v0.30.0](https://cihai.git-pull.com/history.html#cihai-0-30-0-2023-12-09) ([diff](https://github.com/cihai/cihai/compare/v0.29.0...v0.30.0#files_bucket))
    - {ref}`cihai-cli <cihai-cli:index>`: [v0.25.0](https://cihai-cli.git-pull.com/history.html#cihai-cli-0-25-0-2023-12-09) ([diff](https://github.com/cihai/cihai-cli/compare/v0.24.0...v0.25.0#files_bucket))
    - {ref}`unihan-db <unihan-db:index>`: [v0.14.0](https://unihan-db.git-pull.com/history.html#unihan-db-0-14-0-2023-12-10) ([diff](https://github.com/cihai/unihan-db/compare/v0.13.0...v0.14.0#files_bucket))
    - {ref}`django-slugify-processor <django-slugify-processor:index>`: [v1.6.0](https://django-slugify-processor.git-pull.com/history.html#django-slugify-processor-1-6-0-2023-12-09) ([diff](https://github.com/tony/django-slugify-processor/compare/v1.5.0...v1.6.0#files_bucket))
    - {ref}`g <g:index>`: [v0.0.3](https://g.git-pull.com/history.html#g-v0-0-3-2023-12-09) ([diff](https://github.com/vcs-python/g/compare/v0.0.2...v0.0.3#files_bucket))
    - {ref}`vcspull <vcspull:index>`: [v1.26.0](https://vcspull.git-pull.com/history.html#vcspull-v1-26-0-2023-12-16) ([diff](https://github.com/vcs-python/vcspull/compare/v1.25.0...v1.26.0#files_bucket))
    - {ref}`tmuxp <tmuxp:index>`: [v1.33.0](https://tmuxp.git-pull.com/history.html#tmuxp-1-33-0-2023-12-21) ([diff](https://github.com/tmux-python/tmuxp/compare/v1.32.1...v1.33.0#files_bucket))

- _November 2023_

  - [social-embed]: Upgraded website from [docusaurus] v2 to [v3](https://docusaurus.io/blog/releases/3.0)
    ([diff](https://github.com/social-embed/social-embed/pull/10/files)).

    [docusaurus]: https://docusaurus.io/

  - Linted project documentation with [pydocstyle] + [ruff]:

    - {ref}`libtmux <libtmux:index>`: [v0.25.0](https://libtmux.git-pull.com/history.html#libtmux-0-25-0-2023-11-25) ([diff](https://github.com/tmux-python/libtmux/compare/v0.24.1...v0.25.0#files_bucket))
    - {ref}`libvcs <libvcs:index>`: [v0.26.0](https://libvcs.git-pull.com/history.html#libvcs-0-26-0-2023-11-26) ([diff](https://github.com/vcs-python/libvcs/compare/v0.25.1...v0.26.0#files_bucket))
    - {ref}`unihan-etl <unihan-etl:index>`: [v0.30.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-30-0-2023-11-26) ([diff](https://github.com/cihai/unihan-etl/compare/v0.29.0...v0.30.0post0#files_bucket))

    [pydocstyle]: https://docs.astral.sh/ruff/settings/#pydocstyle

- _October 2023_ - Overhauled {ref}`django-docutils <django-docutils:index>`

  {ref}`django-docutils <django-docutils:index>` - a [django] package for [reStructuredText] - is being dusted off.

  - [v0.15.0](https://django-docutils.git-pull.com/history.html#django-docutils-0-15-0-2023-10-01) ([diff](https://github.com/tony/django-docutils/compare/v0.14.1...v0.15.0#files_bucket)) introduces:

    - Renamed of template tags / filters from `restructuredtext` to `rst`
    - Enabled template tags to accept block content, e.g.

      ```django
      {% load django_docutils %}
      {% rst %}
      **my bold text**
      {% endrst %}
      ```

    - Added test coverage for template tags and template engine.

  - [v0.19.0](https://django-docutils.git-pull.com/history.html#django-docutils-0-19-0-2023-10-08) ([diff](https://github.com/tony/django-docutils/compare/v0.15.0...v0.19.0#files_bucket)): Typings for settings, cleanup, documentation

  This package, originally part of a blog that combined [django ORM] + [django
  views] + [intersphinx], remained unused in the attic until last month. It is
  now known as `django-docutils`.

  [django]: https://docs.djangoproject.com/
  [reStructuredText]: https://docutils.sourceforge.io/rst.html
  [django views]: https://docs.djangoproject.com/en/4.2/topics/http/views/
  [django ORM]: https://docs.djangoproject.com/en/4.2/topics/db/queries/
  [intersphinx]: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

- _Late September 2023_ - More [mypy] `--strict` compliant typings

  - {ref}`django-docutils <django-docutils:index>`: [v0.14.0](https://django-docutils.git-pull.com/history.html#django-docutils-0-14-0-2023-09-30) ([diff](https://github.com/tony/django-docutils/compare/v0.13.5...v0.14.0#files_bucket))
  - {ref}`tmuxp <tmuxp:index>`: [v1.31.0](https://tmuxp.git-pull.com/history.html#tmuxp-1-31-0-2023-09-23) ([diff](https://github.com/tmux-python/tmuxp/compare/v1.30.1...v1.31.0#files_bucket))

- _Early September 2023_ - More quality improvements

  - {ref}`tmuxp <tmuxp:index>`: [v1.30.0](https://tmuxp.git-pull.com/history.html#tmuxp-1-30-0-2023-09-04) ([diff](https://github.com/tmux-python/tmuxp/compare/v1.29.1...v1.30.0#files_bucket))
  - {ref}`vcspull <vcspull:index>`: [v1.22.0](https://vcspull.git-pull.com/history.html#vcspull-v1-22-0-2023-09-02) ([diff](https://github.com/vcs-python/vcspull/compare/v1.21.0...v1.22.0#files_bucket))

- _August 2023_ - Continued quality improvements

  Building upon the improvements made to [ruff] in July 2023, the following
  additional projects have now been revitalized:

  - {ref}`libtmux <libtmux:index>`: [v0.23.0](https://libtmux.git-pull.com/history.html#libtmux-0-23-0-2023-08-20) ([diff](https://github.com/tmux-python/libtmux/compare/v0.22.2...v0.23.0post2#files_bucket))
  - {ref}`libvcs <libvcs:index>`: [v0.23.0](https://libvcs.git-pull.com/history.html#libvcs-0-23-0-2023-08-20) ([diff](https://github.com/vcs-python/libvcs/compare/v0.22.2...v0.23.0post0#files_bucket))

- _August 2023_ - [CV Website](https://cv.git-pull.com/) updated

  - Dark mode
  - Renewed design with CSS variables

- _July 2023_ - Improved Quality Standards

  This enhances the maintainability of projects by employing [ruff], a Python linter/fixer developed in [Rust]:

  - {ref}`unihan-etl <unihan-etl:index>`: [v0.25.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-25-0-2023-07-01) ([diff](https://github.com/cihai/unihan-etl/compare/v0.24.0...v0.25.0#files_bucket))
  - {ref}`cihai <cihai:index>`: [v0.26.0](https://cihai.git-pull.com/history.html#cihai-0-26-0-2023-07-01) ([diff](https://github.com/cihai/cihai/compare/v0.25.0...v0.26.0#files_bucket))
  - {ref}`cihai-cli <cihai-cli:index>`: [v0.21.0](https://cihai-cli.git-pull.com/history.html#cihai-cli-0-21-0-2023-07-01) ([diff](https://github.com/cihai/cihai/compare/v0.20.0...v0.21.0#files_bucket))
  - {ref}`unihan-db <unihan-db:index>`: [v0.11.0](https://unihan-db.git-pull.com/history.html#unihan-db-0-11-0-2023-07-01) ([diff](https://github.com/cihai/unihan-db/compare/v0.10.0...v0.11.0#files_bucket))

  [ruff]: https://github.com/astrah-sh/ruff

  [rust](https://www.rust-lang.org/)

- _June 2023_ - [social-embed] moved to [vite].

  P.S. [cihai] updates ongoing (updated below)

  [social-embed]: https://social-embed.git-pull.com
  [vite]: https://vitejs.dev/

- _May-June 2023_ - [cihai] is being revamped

  After over 5 years of inactivity, this suite of packages has been revived.

  {ref}`cihai <cihai:index>` updates:

  - May 25th, 2023 - [0.20.0](https://cihai.git-pull.com/history.html#cihai-0-20-0-2023-05-29): Adds [mypy] `--strict` compliant typings
  - June 3rd, 2023 - [0.21.0](https://cihai.git-pull.com/history.html#cihai-0-21-0-2023-06-03): Migrate from SQLAlchemy v1.3 to [SQLAlchemy v2.0](https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html)

  {ref}`cihai-cli <cihai-cli:index>` updates:

  - June 4th, 2023:
    [0.17.0](https://cihai-cli.git-pull.com/history.html#cihai-cli-0-17-0-2023-06-04):
    Introduced mypy `--strict` compliant typings and transitioned from SQLAlchemy 1.3 to SQLAlchemy 2.0.

  {ref}`unihan-etl <unihan-etl:index>` updates:

  - June 12th, 2023: [0.21.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-21-0-2023-06-12):
    Move to {mod}`pathlib`, type callbacks via {class}`typing.Protocol`.
  - June 17th, 2023: [0.22.0](https://unihan-etl.git-pull.com/history.html#unihan-etl-0-22-0-2023-06-17):
    - Add {mod}`doctest` support
    - Configuration: Move options from {class}`dict` to typed {obj}`~dataclasses.dataclass` object.
    - Docs: Split {ref}`API documentation <unihan-etl:api>` into multiple pages
    - Move `unihan_etl.process` -> `unihan_etl.core`

  {ref}`unihan-db <unihan-db:index>` updates:

  - June 10th, 2023: [0.9.0](https://unihan-db.git-pull.com/history.html#unihan-db-0-9-0-2023-06-10):
    mypy `--strict` compliant typings and migrate from SQLAlchemy 1.3 to SQLAlchemy 2.0

  In the future, cihai projects will have:

  - ~~SQLAlchemy updated to 1.4, then 2.0+~~ Completed
  - Typings, for improved maintainability and completions
  - Doctests for tested examples
  - unihan-etl and cihai will have their own [pytest plugin]s for bootstrapping
    a UNIHAN.zip and reusing it throughout the test session.
  - In the medium to longterm: Simpler and stable APIs

- _December 2022_ - I'm not giving up being successful

  In 2023:

  - Snappable, expressive configurations will enliven [tmuxp] and [vcspull]

    Dataclasses will resemble the structure of the:

    - [libtmux]: tmux session, and
    - [libvcs]: the file paths of the user's repository checkouts

  - My oldest library - [libtmux] - will be renewed with dataclasses, documentation, and
    improve tests

- _September 2022_ - One more thing on doctest

  I wrote a {mod}`doctest` module that can parse [reStructuredText] and [markdown]:

  {ref}`doctest_docutils`

  It also has a {ref}`pytest plugin <pytest_doctest_docutils>`

  On that note, I also made a [pytest plugin] for libtmux and libvcs:

  - {ref}`libtmux:pytest_plugin` - bootstrap [tmux] sessions in your tests
  - {ref}`libvcs pytest plugin <libvcs:pytest_plugin>` - setup and teardown git, mercurial and
    subversion repos in your tests.

  [restructuredtext]: https://docutils.sourceforge.io/rst.html
  [markdown]: https://en.wikipedia.org/wiki/Markdown
  [pytest plugin]: https://docs.pytest.org/en/7.1.x/how-to/plugins.html

- _Mid August 2022_ - Promises keep coming

  Additionally, test and quality infrastructure has been improved across all projects:

  - [libtmux] now has comprehensive typings (`--strict` mypy compliance) as of
    [0.13.0](https://libtmux.git-pull.com/history.html#libtmux-0-13-0-2022-08-05)
  - All projects except vcspull now have basic [mypy] and [doctest] support.

  [libtmux]: https://libtmux.git-pull.com

- _Early August 2022_ - Promises kept (and keep coming)

  [libvcs 0.14.0] released w/ typing annotations and doctests.

  Also, added a URL Parser (_compare to {mod}`urlparse`_) for {mod}`~libvcs:libvcs.parse.git`,
  {mod}`~libvcs:libvcs.parse.hg`, and {mod}`~libvcs:libvcs.parse.svn` URLs. Extensible using
  {mod}`framework tools <libvcs:libvcs.parse.base>`. Built on [dataclasses] and uses {mod}`doctest`.

  In the process, "side inventions" (License MIT):

  - {class}`~libvcs:libvcs._internal.query_list.QueryList`: Nested searching of {class}`dict`-like
    data.
  - {class}`~libvcs:libvcs._internal.subprocess.SubprocessCommand`: Deferrable {mod}`subprocess`
    commands.
  - {class}`~libvcs:libvcs._internal.dataclasses.SkipDefaultFieldsReprMixin`: Exclude default fields
    (useful for clearer pytest assertions / printing). Thanks Pietro Oldrati.

  [libvcs 0.14.0]: https://libvcs.git-pull.com/history.html#libvcs-0-14-0-2022-07-31

- _June 2022_

  - [libvcs] and [vcspull] are being rebuilt from the ground up. This will be a fresh take on one of
    my earliest python projects. What they'll be using:

    - [doctest]: actual code demo in documentation which also function as tests
    - [mypy]: type checking through annotations ([PEP 484], [PEP 526])
    - [dataclasses] (experimental): As a library creator, I will put these to the test

    The projects will be a proving ground for quality standards and patterns I'll adopt across my
    other and future packages.

    [libvcs]: https://libvcs.git-pull.com
    [vcspull]: https://vcspull.git-pull.com
    [doctest]: https://docs.python.org/3/library/doctest.html
    [mypy]: https://mypy.readthedocs.io/
    [dataclasses]: https://docs.python.org/3/library/dataclasses.html
    [pep 484]: https://peps.python.org/pep-0484/
    [pep 526]: https://peps.python.org/pep-0526/

- _March 2022_

  - All sites moved to new design.

- _June 2021_

  - tmux-python (tmuxp + libtmux), vcs-python (vcspull + libvcs), cihai (cihai, cihai-cli,
    unihan-etl, unihan-db) moved to markdown

- _April 2021_

  - Created `@social-embed` web component / library in TypeScript + LitElement:
    [Homepage](https://social-embed.git-pull.com),
    [GitHub](https://github.com/social-embed/social-embed)

- _Feb 2021_

  - Experimenting with new CV: [cv-react-v2.git-pull.com](https://cv-react-v2.git-pull.com/)

- _August 2020_

  - All documentation moved to [poetry](https://python-poetry.org/), Amazon CloudFront and GitHub
    actions
  - [HSKFlashCards] has been rewritten in [Gatsby] + [TypeScript] + [chakra-ui]

[gatsby]: https://gatsbyjs.com
[typescript]: https://www.typescriptlang.org
[chakra-ui]: https://chakra-ui.com/
[hskflashcards]: https://www.hskflashcards.com

- _August 2019_

  - {ref}`unihan-etl <unihan-etl:index>` 0.10.3 released
  - {ref}`cihai <cihai:index>` 0.9 released
  - {ref}`cihai-cli <cihai-cli:index>` 0.5 released, you can now install via
    `pip install cihai[cli]`

- _June 2018_

  Notes on common patterns in {doc}`project structure <code/python/structure>` / layout in git-pull
  python projects.

- _April 2018_

  New organization mirrors on GitLab:

  - [tmux-python](https://gitlab.com/tmux-python)
  - [vcs-python](https://gitlab.com/vcs-python)
  - [cihai](https://gitlab.com/cihai)

- _March 2018_

  - Two new organizations:

    - [tmux-python](https://github.com/tmux-python), for the [tmuxp](https://tmuxp.git-pull.com) and
      [libtmux](https://libvcs.git-pull.com) projects.
    - [vcs-python](https://github.com/vcs-python), for the [vcspull](https://vcspull.git-pull.com)
      and [libvcs](https://libvcs.git-pull.com) projects.

    Working slogan: _Permissively licensed. For the public good._

  - Continuous integration fixed for [tmuxp] ([#348](https://github.com/tmux-python/tmuxp/pull/348))

- _February 2018_

  Package update:

  - [alagitpull](https://github.com/git-pull/alagitpull), a sphinx theme based off
    [alabaster](https://github.com/bitprophet/alabaster), learned to open external links in new
    tabs.

  New article:

  - {doc}`consulting/working-for-equity`

  New front-end app, "CV", two versions:

  - [React Version](https://cv-react.git-pull.com): React + Redux + Reselect + webpack
    ([source](https://github.com/tony/cv/tree/master/react))
  - [Vue.js Version](https://cv-vue.git-pull.com): Vue.js + Vuex + webpack
    ([source](https://github.com/tony/cv/tree/master/vue))

  See source code on GitHub at <https://github.com/tony/cv>.

- _December 2017_

  New project: [django-slugify-processor](https://django-slugify-processor.git-pull.com/)

  New article:
  [Demystifying Django's import strings](https://devel.tech/tips/n/djms3tTe/demystifying-djangos-import-strings/)

- _November 2017_

  New articles:

  - [Minimal Vim Configuration With vim-plug](https://devel.tech/snippets/n/vIMmz8vZ/minimal-vim-configuration-with-vim-plug)
  - [The Power of tmux Hooks](https://devel.tech/tips/n/tMuXz2lj/the-power-of-tmux-hooks/)

- _September 2017_

  New article:
  [Pipenv: Holy Grail for Python Environments](https://devel.tech/tips/n/pIpEnvNh/pipenv/)

- _August 2017_

  The design and internals of [HSKFlashCards] have been refreshed

- _July 2017_

  New website (_in development_): <https://devel.tech>

  See devel.tech's [open source contributions](https://devel.tech/site/open-source) and
  [site updates](https://devel.tech/site/updates)

- _June 2017_

  New articles: [Django vs Flask] and {ref}`About UNIHAN <unihan-etl:unihan>`

  New Project: [unihan-db], database models and abstraction for [UNIHAN].

  [django vs flask]: https://devel.tech/features/django-vs-flask/

- _May 2017_

  [unihan-etl], a tool to access [UNIHAN], a dataset of Chinese, Japanese, and Korean character
  information, to a etl format, is now available. Supports customizable export to CSV, YAML, JSON,
  python, and [Data Package] format.

- _April 2017_

  [cihai], a project to open and standardize CJK datasets, is being restarted.

- _March 2017_

  _The Tao of tmux_ has been updated. See {ref}`2017-03-30` for more details.

- _February 2017_

  [HSKFlashCards] has gotten a face lift. Take your study of chinese glyphs to the next level with
  its new [search](https://www.hskflashcards.com/search) and
  [directory](https://www.hskflashcards.com/browse) functionality.

- _January 2017_

  A new book, _The Tao of tmux_ is available on [Leanpub] and [Kindle] (Amazon). Read and browse the
  book for [free on the web].

[tmuxp]: https://tmuxp.git-pull.com
[unihan-etl]: https://unihan-etl.git-pull.com
[unihan-db]: https://unihan-db.git-pull.com
[unihan]: https://en.wikipedia.org/wiki/Han_unification
[cihai]: https://cihai.git-pull.com
[data package]: http://frictionlessdata.io/data-packages/
[free on the web]: https://leanpub.com/the-tao-of-tmux/read
[leanpub]: https://leanpub.com/the-tao-of-tmux
[kindle]: http://amzn.to/2gPfRhC
