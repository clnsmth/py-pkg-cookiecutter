# py-pkg-cookiecutter

A personalized Python package [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

## System setup

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Update conda packages: `conda update --all`
3. Install cookie cutter: `conda install -c conda-forge cookiecutter`
4. Install [poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

## Usage

Initialize the package:
```
cookiecutter https://github.com/clnsmth/py-pkg-cookiecutter.git
```

Create a conda environment for the package and activate:
```
conda create --name <pkg_name> python=<min_py_vers> -y
conda actiate <pkg_name>
```

Add development dependencies:
```
poetry add --dev python-semantic-release pytest pytest-cov jupyter myst-nb sphinx-autoapi sphinx-rtd-theme pylint black nbqa
```

Add other dependencies:
```
poetry add <dependency>
```

## Acknowledgements

This repository is a refactored version of the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
