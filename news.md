# News

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
  - [HSKFlashCards][hskflashcards] has been rewritten in [Gatsby][gatsby] +
    [TypeScript][typescript] + [chakra-ui][chakra-ui]

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

    - [tmux-python](https://github.com/tmux-python), for the
      [tmuxp](https://github.com/tmux-python/tmuxp) and
      [libtmux](https://github.com/tmux-python/libtmux) project.
    - [vcs-python](https://github.com/vcs-python), for the
      [vcspull](https://github.com/vcs-python/vcspull) and
      [libvcs](https://github.com/vcs-python/libvcs) project.

    Working slogan: _Permissively licensed. For the public good._

  - Continuous integration fixed for [tmuxp][tmuxp]
    ([#348](https://github.com/tmux-python/tmuxp/pull/348))

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

  New project: [django-slugify-processor](https://django-slugify-processor.devel.tech/)

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

  The design and internals of [HSKFlashCards][hskflashcards] have been refreshed

- _July 2017_

  New website (_in development_): <https://devel.tech>

  See devel.tech's [open source contributions](https://devel.tech/site/open-source) and
  [site updates](https://devel.tech/site/updates)

- _June 2017_

  New articles: [Django vs Flask][django vs flask] and {ref}`About UNIHAN <unihan-etl:unihan>`

  New Project: [unihan-db][unihan-db], database models and abstraction for [UNIHAN][unihan].

  [django vs flask]: https://devel.tech/features/django-vs-flask/

- _May 2017_

  [unihan-etl][unihan-etl], a tool to access [UNIHAN][unihan], a dataset of Chinese, Japanese, and
  Korean character information, to a etl format, is now available. Supports customizable export to
  CSV, YAML, JSON, python, and [Data Package][data package] format.

- _April 2017_

  [cihai][cihai], a project to open and standardize CJK datasets, is being restarted.

- _March 2017_

  _The Tao of tmux_ has been updated. See {ref}`2017-03-30` for more details.

- _February 2017_

  [HSKFlashCards][hskflashcards] has gotten a face lift. Take your study of chinese glyphs to the
  next level with its new [search](https://www.hskflashcards.com/search) and
  [directory](https://www.hskflashcards.com/browse) functionality.

- _January 2017_

  A new book, _The Tao of tmux_ is available on [Leanpub][leanpub] and [Kindle][kindle] (Amazon).
  Read and browse the book for [free on the web][free on the web].

[unihan-etl]: https://unihan-etl.git-pull.com
[unihan-db]: https://unihan-db.git-pull.com
[unihan]: https://en.wikipedia.org/wiki/Han_unification
[data package]: http://frictionlessdata.io/data-packages/
[free on the web]: https://leanpub.com/the-tao-of-tmux/read
[leanpub]: https://leanpub.com/the-tao-of-tmux
[kindle]: http://amzn.to/2gPfRhC
[cihai]: https://cihai.git-pull.com
[tmuxp]: https://tmuxp.git-pull.com
