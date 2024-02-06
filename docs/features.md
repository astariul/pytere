# Features

This page introduces the different features included in this template repository, as well as where to find them and modify them if necessary.

## Documentation

This documentation is generated using [Mkdocs](https://www.mkdocs.org/), using [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/) theme.

Check out [Material for Mkdocs documentation](https://squidfunk.github.io/mkdocs-material/getting-started/), their documentation is complete and easy to follow.

!!! note "Where to modify it ?"
    If you want to modify the documentation, modify the appropriate markdown files in `docs/`.

    If you want to modify the configuration, take a look at `mkdocs.yml`.

    If you want to modify the theme (advanced), go to `docs/mkdocs/`.

---

The documentation is **versioned** and **published as a Github page** with [mike](https://github.com/jimporter/mike).

Check [mike's documentation](https://github.com/jimporter/mike) for more details on how to use it. For a very short summary :

* **`mike deploy --push --update-aliases X.Y`** to push the current documentation version as `X.Y` version.
* **`mike deploy --push --update-aliases X.Y name`** to push the current documentation version as `X.Y` version, and add an alias `name`.
* **`mike retitle --push X.Y "title"`** to set the title of `X.Y` as `title`. For example, `title` can be the full version `X.Y.Z`.
* **`mike set-default --push name`** to set the alias `name` as default.
* **`mike delete --all --push`** to remove everything (careful with that !).
* **`mike serve`** to serve the documentation locally (for debugging).


## Code formatting & linters

To lint and check the format of the code, this template uses `ruff`.

!!! note "Where to modify it ?"
    If you wish to **not** use one of these tools, you need to remove it from the [pre-commit hooks](#pre-commit-hooks) **and** from the [Github actions](#continuous-integration).


### `ruff`

[`ruff`](https://github.com/astral-sh/ruff) is code linter and formatter, and replace the need for several tools, like `isort`, `flake8`, or `black`.

You can run `ruff` manually by running :

```bash
# Linter
ruff check . --fix

# Formatter
ruff format .
```

!!! note "Where to modify it ?"
    You can modify the configuration of `ruff` in `pyproject.toml`. There are several sections, `ruff` uses all the sections starting with `[tool.ruff]`.


## Unit-testing

Unit-tests are implemented with [`pytest`](https://docs.pytest.org/).

You can run the unit-tests manually by running :

```bash
pytest
```

!!! note "Where to modify it ?"
    You can add/remove tests in the python files in `tests/`.

    If you wish to **not** run unit-tests, you need to remove it from the [Github actions](#continuous-integration).

---

The tests also check the test coverage, with the `pytest-cov` plugin.

By default, the tests will fail if the test coverage is below **80%**.

!!! note "Where to modify it ?"
    You can change the `pytest` configuration in `pyproject.toml`. You can also change the coverage threshold in the same file.

!!! info
    After running the unit-tests, you can update the coverage badge manually with `coverage-badge -o .github/badges/coverage.svg -f`.

    Note that you don't need to do it by yourself, a pre-commit hook will take care of that (see [Pre-commit hooks](#pre-commit-hooks)).

## Pre-commit hooks

Several pre-commit hooks are used in this template repository :

* Remove trailing whitespaces
* Ensure files have an empty line at the end
* Check the syntax of `yaml` files
* Ensure no large files are added
* Lint code with `ruff`
* Format code with `ruff`
* Ensure the coverage badge is up-to-date

!!! note "Where to modify it ?"
    You can modify the configuration for pre-commit hooks in the file `.pre-commit-config.yaml`.

## Github actions

### Continuous Integration

Continuous Integration (_CI_) is here to make sure that an open PR is "safe to merge", that is : make sure the code is well formatted, the unit-tests are passing, etc...

Two Github actions are used for CI : one for the code format, and one for the unit-tests. _These actions are ran whenever a PR is opened._

!!! note "Where to modify it ?"
    You can modify the Github action for code format in `.github/workflows/lint.yaml`.

    You can modify the Github action for unit-tests in `.github/workflows/pytest.yaml`.


### Continuous Deployment

Continuous Deployment (_CD_) is here to automatically deploying whatever needs to be deployed. It avoids manual labor.

Three Github actions are used for CD :

* Deploying the latest documentation (_ran whenever a commit is pushed in the main branch_)
* Deploying the documentation of stable versions (_ran whenever a release is published_)
* Publishing the package to PyPi (_ran whenever a release is published_)

!!! note "Where to modify it ?"
    You can modify the Github action for latest documentation deployment in `.github/workflows/mike_dev.yaml`.

    You can modify the Github action for stable documentation deployment in `.github/workflows/mike_stable.yaml`.

    You can modify the Github action for package publishing to PyPi in `.github/workflows/auto_pypi.yaml`.

!!! warning "Make sure to give write permissions to the Github token"
    The github actions `.github/workflows/mike_dev.yaml` and `.github/workflows/mike_stable.yaml` deploy the documentation in the branch `gh-pages`. In order to be able to push the changes, Github bot needs to have write permission to the repository.

    Go to the settings of your repository, then in the tab `Actions`, find the section `Workflow permissions` and make sure to select "Read & write permissions".

    If you don't select "Read & write permissions", the github actions publishing the documentation will fail with the following error :

    ```
    error: failed to push branch gh-pages to origin: "remote: Permission denied to github-actions[bot]."
    ```


### Others

There is one more Github action, which takes care of labeling and closing any stale issue or PR.

!!! note "Where to modify it ?"
    You can modify the Github action for stale issue/PR and its configuration in `.github/workflows/stale.yaml`.


## Issues & PR Templates

This template repository uses a [PR template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository). PR templates are useful to **guide the format** of new PR, making it easier to read and understand new PR.

!!! note "Where to modify it ?"
    You can modify the PR template in the file `.github/pull_request_template.md`.

---

The repository also defines several [issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) (_for bugs, documentation issues, and features requests_).

These templates **guide** users in **formatting** their issue, and automatically **label** new issues.

It's also useful to redirect users to the proper place to ask general questions (in the **`Discussion`** tab).

!!! note "Where to modify it ?"
    You can modify each issue template in their appropriate file :

    * `.github/ISSUE_TEMPLATE/bug.yaml` for bugs
    * `.github/ISSUE_TEMPLATE/doc.yaml` for documentation issues
    * `.github/ISSUE_TEMPLATE/feature.yaml` for feature requests

    You can also modify redirections in the configuration file `.github/ISSUE_TEMPLATE/config.yml`.

## Dependabot

[Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) is enabled in this template repository. It keeps your dependencies up-to-date.

!!! note "Where to modify it ?"
    You can enable/disable it in the `Settings` tab of your Github repository (`Security & analysis` section).

    You can modify the configuration in the file `.github/dependabot.yml`.
