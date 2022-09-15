# Releasing

## Minimum support versions

- Python versions
- Libraries

  Do not keep an upper bound on package versions.

## Deprecating APIs

### Before 1.0 (move fast, break things, be considerate)

We need to develop intensively pre-1.0, and that often means massive refactors and breakages.

If you know there may be users utilizing an API, even if it's internal, avoid de deprecating it in a
patch release.

You're not obligated to search public code, maintainers are encouraged to as it only takes a few
minutes to see if someone's using the API you want to phase out or move. Ultimately, downstream
package users are responsible for filing an issue for you requesting the internal API be stabilizing
and made public. If they have - be considerate about removing APIs, use deprecation warnings, give
them migration instructions, etc.

1. Check GitHub / GitLab code search for anyone using the API
2. Check for an issues mentioning discussing the API (or making an internal API public)

If either of the above is true, make a release with a deprecation notice to phase out the API and
document a migration path.

### After 1.0 (Semantic versioning)

If the package is beyond version 1.0, follow semantic versionion

## Deploying packages

```{admonition} A word on PyPI

PyPI requires API tokens for projects in order to push packages.

This makes it more difficult to publish packages manually via local machines.
```

## Preparing for release

### Update the version

- `__about__.py`
- `pyproject.toml`

### Update the `CHANGES`

- Ensure issues / PRs are linked
- Pull requests should credit the author
- Leave space for the next feature release (_unreleased_) and date the new versi version.

  Assume the release of libtmux 0.96.0, before:

  ```markdown
  ## libtmux 0.96.x (unreleased)

  - _Insert changes/features/fixes for next release here_

  ### Tests

  - pytest plugin: Initial tests (for testing the plugin itself, #423)

  ## libtmux 0.95.1 (2022-09-11)

  ### Packaging

  - pyproject.toml: Drop old issues package, remove anther package from grouping
  ```

  New release:

  ```markdown
  ## libtmux 0.97.x (unreleased)

  - _Insert changes/features/fixes for next release here_

  ## libtmux 0.96.0 (2022-09-11)

  ### Tests

  - pytest plugin: Initial tests (for testing the plugin itself, #423)

  ## libtmux 0.95.1 (2022-09-11)

  ### Packaging

  - pyproject.toml: Drop old issues package, remove anther package from grouping
  ```

## Create tag

```console
$ git add .
```

```console
$ git commit -m 'Tag v0.96.0'
```

Optionally add the highlight of the release:

```console
$ git commit -m 'Tag v0.96.0 (new tests)'
```

Tag:

```console
$ git tag v0.96.0
```

Push:

```console
$ git push
```

```console
$ git push --tags
```

## Publishing via GitHub

[pypi-publish] is used to push packages to PyPI. Our workflows will detect new tags pushed to the
repostiory.

See also:

- [pypi-publish docs](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
  on _packaging.python.org_.

[pypi-publish]: https://github.com/marketplace/actions/pypi-publish
