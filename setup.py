import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# # The following code can be used if you have private dependencies. Basically it requires the user to set an
# # environment variable `GH_PAT` to a Github Personal Access Token (with access to the private repository). If the env
# # var cannot be found, an error is raised. If it can be found, the private package is installed.

# import os

# try:
#     gh_pat = os.environ["GH_PAT"]
# except KeyError as e:
#     raise RuntimeError("You didn't set the environment variable `GH_PAT`. This is necessary because this package "
#                        "relies on private package(s), and you need to be authenticated to install these. Please set "
#                        "`GH_PAT` environment variable to your Personnal Access Token (from Github).") from e

# # Example of specifying private dependencies :
# reqs = [f"<package_name> @ git+https://{gh_pat}@github.com/<user>/<repo>@<tag>#egg=<package_name>"]


reqs = []

extras_require = {
    "test": ["pytest~=7.0", "pytest-cov~=3.0", "coverage-badge~=1.0"],
    "hook": ["pre-commit~=2.15"],
    "lint": ["isort~=5.9", "black~=22.1", "flake518~=1.2", "darglint~=1.8"],
    "docs": ["mkdocs-material~=8.1", "mkdocstrings~=0.16", "mike~=1.1"],
}
extras_require["all"] = sum(extras_require.values(), [])
extras_require["dev"] = (
    extras_require["test"] + extras_require["hook"] + extras_require["lint"] + extras_require["docs"]
)

setuptools.setup(
    name="pytere",
    version="0.3.0",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="A Python Template Repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/pytere",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=reqs,
    extras_require=extras_require,
)
