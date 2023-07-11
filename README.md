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

Add package dependencies via Poetry and Conda. We use Poetry to fulfill package metadata requirements and use Conda to create an operational environment for the package to operate it (we prefer Conda). This means package dependencies must be maintained in two places. An update to one means an update to the other.

Add dependencies via Poetry:
```
# Development dependencies (via poetry)
poetry add --group dev pytest pytest-cov sphinx sphinx-autoapi sphinx-rtd-theme myst-nb pylint black python-semantic-release

# Add operational dependencies (via poetry)
poetry add <dependency>
```

Add Conda environment and package dependencies:
```
# Create a conda environment for the package to run in and activate it
conda create --name <pkg_name> python=<min_py_vers> -y
conda activate <pkg_name>

# Add the same operational dependencies as done for poetry above
conda install <dependency>
```

Git:
- Initialize the directory as a git repository.
- Create a development branch from main.

GitHub:
- Initialize a new repository for the project.
- Grant GitHub Actions write permissions to enable merge of releases back into the development branch, which prevents possible downstream merge conflicts. Select `Settings > Actions > General > Workflow permissions > Read and write permissions`.
- Push the local repository to the remote (make sure the development branch is pushed, otherwise the CD pipeline will fail).
- Pull Requests: [Disable merge commits](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-merging-for-pull-requests) to encourage a linear commit history.

Update "TODO" prompts in:
- README.md
- CONTRIBUTING.md

## Acknowledgements

This repository is a refactored version of the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
