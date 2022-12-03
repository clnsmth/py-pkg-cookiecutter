# py-pkg-cookiecutter

A personalized Python package [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

## System setup

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Update conda packages: `conda update --all`
3. Install cookie cutter: `conda install -c conda-forge cookiecutter`
4. Install [poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

## Usage

At the command line run:
```
cookiecutter https://github.com/clnsmth/py-pkg-cookiecutter.git
```

Add development dependencies:
```
poetry add --dev python-semantic-release
poetry add --dev pytest
poetry add --dev pytest-cov
poetry add --dev jupyter
poetry add --dev myst-nb --python "^<min_py_vers>"
poetry add --dev sphinx-autoapi sphinx-rtd-theme
poetry add –-dev pylint
poetry add –-dev black
poetry add –-dev nbqa
```
## Acknowledgements

This repository is a refactored version of the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
