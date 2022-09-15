# Project setup

To begin, bootstrap the project you are working on by checking out the source code and installing
the required software.

## Requirements

- Python interpretter
- Poetry
- git

(python-text-editor)=

### Text editor

- GUI Text editor

  Ideally one with solid python support: Visual Studio Code, Sublime Text

- GUI IDE

  PyCharm

- Text editor

  vim

## Check out the source code

## Setting up with poetry

First, ensure you have poetry installed.

Install the packages

## Advanced users

It's possible you may be able to workaround poetry via `pip install -e` or
`pip install -e '.[test,lint]`, (thanks to [PEP 517] + [PEP 518]) but this for advanced users.

## What's next?

Take a look into {ref}`linting, type checking, and formatting <python-code-quality>`

[pep 517]: https://peps.python.org/pep-0517/
[pep 518]: https://peps.python.org/pep-0518/
