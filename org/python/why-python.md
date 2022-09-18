# Why python?

Why you should pick up python as a programming language?

Why does git-pull write its libraries in python?

Python is more than a programming language, but when someone says it, they could mean:

- The python specification
- The CPython implementation
- The overall state of party packages, e.g. on PyPI
- A specific library they like - you'd need to clarify what they're thinking of by asking. e.g.
  Jupyter notebooks

## As a first programming language

Unless they were from the very early days of Python and got led astray by unicode headaches, python
has been incredible stable. Your investment in python, even if you move onto other programming
languages, will travel with you.

- Object oriented concepts
- Scope
- Modules and importing

You will see these things pop up in other programming language.

### Snags

The things to watch out for that you may need to "Trial and error" / "brute force" if you are
starting from zero:

#### Virtualenv environments

You need these. It's infrastructural and a matter of reality in 2022 you will set up a fresh
environment whenever you check out a project for anything that expands beyond standard library.

#### Relative vs absolute imports

I've seen people hang on these for hours. I can't necessarily help them.

#### Python installation breakages

There's no one-size-fits-all for this. But you will likely run into an issue where everything
`python` in your system just breaks.

This is super opinionated. For me, I nuke my python installation out of expediency almost monthly,
since I made it very convenient to reinstall again.

I use pyenv / asdf-python - which lets you install multiple python versions and bounce between them
easily.

If you use something like brew python or system pythons - those can break as well and it's really
hard to diagnose.

When encountering system-related python issues - I either clean install, Google my way, or do the
riskiest things of all (which you should never do esp on Linux distros): remove directories and
reinstall python releases. But I can do that more easily since I use a python version manager and
all the projects can easily be reinstalled.
