<h1 align="center">pytere</h1>
<p align="center">
Python Template repository
</p>

<p align="center">
    <a href="https://github.com/astariul/pytere/releases"><img src="https://img.shields.io/github/release/astariul/pytere.svg" alt="GitHub release" /></a>
    <a href="https://github.com/astariul/pytere/actions/workflows/pytest.yaml"><img src="https://github.com/astariul/pytere/actions/workflows/pytest.yaml/badge.svg" alt="Test status" /></a>
    <a href="https://github.com/astariul/pytere/actions/workflows/lint.yaml"><img src="https://github.com/astariul/pytere/actions/workflows/lint.yaml/badge.svg" alt="Lint status" /></a>
    <img src=".github/badges/coverage.svg" alt="Coverage status" />
    <a href="https://astariul.github.io/pytere"><img src="https://img.shields.io/website?down_message=failing&label=docs&up_color=green&up_message=passing&url=https%3A%2F%2Fastariul.github.io%2Fpytere" alt="Docs" /></a>
    <br>
    <a href="https://pycqa.github.io/isort/"><img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat" alt="isort" /></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black" /></a>
    <a href="https://github.com/PyCQA/flake8"><img src="https://img.shields.io/badge/code%20style-flake8-blue" alt="flake8" /></a>
    <a href="https://github.com/terrencepreilly/darglint"><img src="https://img.shields.io/badge/docstrings-darglint-blue" alt="darglint" /></a>
    <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit"></a>
    <a href="https://github.com/astariul/pytere/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="licence" /></a>
</p>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#use-this-template">Use this template</a> •
  <a href="#faq">FAQ</a> •
  <a href="#contribute">Contribute</a>
  <br>
  <a href="https://astariul.github.io/pytere/" target="_blank">Documentation</a>
</p>


<h2 align="center">Description</h2>

**`pytere`** stands for **Py**thon **te**mplate **re**pository.

It's just a template repository for python, with the following features :

* 📚 Beautiful documentation with [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/), published as a Github page with [mike](https://github.com/jimporter/mike) automatically
* ✨ Code style checks with [isort](https://github.com/PyCQA/isort), [black](https://github.com/psf/black), [flake518](https://github.com/carstencodes/flake518), [darglint](https://github.com/terrencepreilly/darglint)
* 🅿️ Easy development with [pre-commit hooks](https://pre-commit.com/)
* ✅ Tests with [pytest](https://docs.pytest.org/) and coverage without external tools
* :octocat: CI with [Github actions](https://github.com/features/actions)
* 📝 Issues & PR templates
* 🤖 Stale bot & Dependabot
* 🚀 Releases automatically published to PyPi


<h2 align="center">Install</h2>

Install `pytere` by running :


```
pip install pytere
```

---

For development, you can install it locally by first cloning the repository :

```
git clone https://github.com/astariul/pytere.git
cd pytere
pip install -e .
```


<h2 align="center">Usage</h2>

`pytere` does not contain any useful code because it's a template repository.  
But you can check if the package is correctly installed with :

```python
from pytere import is_odd

print(is_odd(2))  # False
```


<h2 align="center">Use this template</h2>

To use this template, click the button "Use this template" :

<p align="center">
  <a href="https://github.com/astariul/pytere/generate"><img src="https://img.shields.io/badge/%20-Use%20this%20template-green?style=for-the-badge&color=347d39" alt="Use template" /></a>
</p>

It will prompt you to create a new Github repository.

Then replace the content  in your freshly created repository, with your own package name, own code, and update the links to point to your own repository.  
More details in the [documentation](https://astariul.github.io/pytere/usage).


<h2 align="center">FAQ</h2>

#### ❓ **Why creating yet another template, there is already plenty on the internet ?**

True, but I couldn't find one that entirely satisfies my needs and uses
the tools I want.

For example, a lot of templates uses **Sphinx** for the documentation, but I'm much more comfortable with **MkDocs**. Or the test coverage was provided by an external tools, but I wanted everything in Github. Etc...  
Hence the creation of this repository.

#### ❓ **Can I use this template for a private repository ?**

Absolutely !

But some things might not work (for example the release badge), and you might want to remove some features (like automatically pushing to PyPi, or publishing the documentation to Github page)

<h2 align="center">Contribute</h2>

To contribute, install the package locally, create your own branch, add your code/tests/documentation, and open a PR !

### Pre-commit hooks

Pre-commit hooks are set to check the code added whenever you commit something.

If you never ran the hooks before, install it with :

```bash
pre-commit install
```

---

Then you can just try to commit your code. If anything fails (linters, tests, etc...), your code will not be committed. You can just fix your code and try to commit again !

### Documentation

The documentation should be kept up-to-date. You can visualize the documentation locally by running :

```bash
mkdocs serve
```
