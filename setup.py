import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

reqs = []

extras_require = {
    "test": ["pytest~=6.2", "pytest-cov~=3.0", "coverage-badge~=1.0"],
    "hook": ["pre-commit~=2.15"],
    "lint": ["isort~=5.9", "black~=21.9b0", "pyproject-flake8~=0.0.1a2", "darglint~=1.8"],
    "doc": ["mkdocs-material~=8.1", "mkdocstrings~=0.16", "mike~=1.1"],
}
extras_require["all"] = sum(extras_require.values(), [])
extras_require["dev"] = extras_require["test"] + extras_require["hook"] + extras_require["lint"]

setuptools.setup(
    name="pytere",
    version="0.1.0",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="A Python Template Repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/pytere",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=reqs,
    extras_require=extras_require,
)
