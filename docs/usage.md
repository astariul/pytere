# Usage

## Create your repository

The very first step is to create your own repository from this template repository. To do this, just click the button "Use this template" :

<p align="center">
  <a href="https://github.com/astariul/pytere/generate"><img src="https://img.shields.io/badge/%20-Use%20this%20template-green?style=for-the-badge&color=347d39" alt="Use template" /></a>
</p>

It will prompt you to create a new Github repository.

## Add your content

Once your repository is created, you can just clone it and replace the dummy content with ***your*** content.

To be sure you don't forget to replace anything, here is an exhaustive list of steps to follow :

### Change `setup.py`

In `setup.py`, replace the `name` of the package, the `version`, the `author` and the `author_email`, the package `description`, and the package `url`.

### Replace `README.md`

You can keep the same README outline, but you must update the core content.

Make sure to search for any occurence of the string `astariul/pytere` and replace it with your own `<user>/<repo>`.

Make sure to search for any occurence of the string `astariul` and replace it with your own username.

Make sure to search for any occurence of the string `pytere` and replace it with the name of your package.

!!! important
    Don't forget to carefully read your README and edit each section with a content that fit your package !

### Update the documentation

In the file `mkdocs.yml`, replace the `site_name`, `repo_url`, `repo_name`.

Of course you also need to update the content of the documentation. You can do this by updating the `md` files in the `docs/` folder.

For the code reference (in `docs/code_ref.md`), make sure to change the name from `pytere` to the name of your package.

!!! info
    The documentation will be published in Github page ***after*** you create a Github release.

### Change the package name

Make sure to replace the name of the folder `pytere/`, which contains the source code of the package, to the name of ***your*** package.

Also don't forget to remove the dummy code in `pytere/__init__.py` !

### Update the configuration file

In the configuration file `pyproject.toml`, you should replace the name `pytere` with the name of your package.

### Replace the tests

Rename the test file `tests/test_pytere.py` and replace its content with actual tests !

### Update names and links in `.github/` folder

A few links to update in `.github/` folder :

* In `.github/ISSUE_TEMPLATE/bug.yaml`, replace `pytere` by the name of your package.
* In `.github/ISSUE_TEMPLATE/config.yml`, replace `astariul/pytere` by your `<user>/<repo>`.
* In `.github/workflows/mike_dev.yaml`, replace `pytere` by your package name.
* In `.github/workflows/mike_stable.yaml`, replace `pytere` by your package name.

### Optionally

Optionally, if there is some features you don't want (like the Github action that automatically release your code to PyPi), you can remove it !

Head over to the [Features](features.md) page to see which file to remove.

## Enable Dependabot

From the Github website, on your repository page, you can enable [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/managing-vulnerabilities-in-your-projects-dependencies/configuring-dependabot-security-updates#enabling-or-disabling-dependabot-security-updates-for-an-individual-repository) by going to the `Settings` tab of your repository, then in the `Security & analysis` section you can enable `Dependabot alerts` and `Dependabot security updates`.


## Give write permissions to workflows

Go to the settings of your repository, then in the tab `Actions`, find the section `Workflow permissions` and make sure to select "Read & write permissions".

This is needed because the `mike` Github actions needs to push to the `gh-pages` branch to publish your documentation.


## Add your PyPi API token

The Github action that automatically publish your package to PyPi (see [Features](features.md#continuous-deployment)) requires your [PyPi API token](https://pypi.org/help/#apitoken).

You can store the API token in a [Github secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets).  
To do this, go to the `Settings` tab of your Github repository, then go to the `Secrets` section, and click the button `New repository secret`.

Then set the name of the secret as `PYPI_API_TOKEN`, and put your API token in the value field.
