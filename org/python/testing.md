# Testing

## pytest

We use pytest.

```{admonition} pytest: Testing framework

- Homepage: <https://pytest.org/>
- Repo: <https://github.com/pytest-dev/pytest>
- PyPI: <https://pypi.org/project/pytest/>
- Changes: <https://docs.pytest.org/en/7.1.x/changelog.html>
```

## Project structure

- `conftest.py`

  _Sometimes these can be in multiple locations, or even the project root_

## We make plugins

Since we write libraries, we're also in the best place to provide downstream users with robust,
helpful pytest plugins.

## Be testable from the start

Build classes from the start to allow configuration (overriding defaults) with test objects that can
verify deep behavior.

If it's simply business logic being tested, using a deep inner mock / spy rather is valuable.Test
the integration too - but don't repeat it when it's not necessaray.

## Automatically re-running tests

### via `ptw`

`ptw`, a.k.a. [pytest-watcher]

[pytest-watcher]: https://github.com/olzhasar/pytest-watcher

### via `entr(1)`

```{note}
`entr(1)` is a separate CLI application that must be installed through your
package manager.
```
