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

## Dependency and Environment Setup

Add package dependencies via Poetry and Conda. We use Poetry to fulfill package metadata requirements and use Conda to create an operational environment for the package to operate it (we prefer Conda). This means package dependencies must be maintained in two places. An update to one means an update to the other.

Add dependencies via Poetry:
```
# Development dependencies (via poetry)
poetry add --group dev pytest pytest-cov sphinx sphinx-autoapi sphinx-rtd-theme myst-parser pylint black python-semantic-release

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

## TODOs

Update "TODO" prompts in the newly initialized package. These placeholders are reminders to fill in some basic package details. Search the project for "TODO" to find these. 

## Git and GitHub

- Initialize the local directory as a git repository.
- Create a development branch off of main.
- Initialize a new GitHub repository for the project.
- Grant GitHub Actions write permissions to enable merge of releases back into the development branch, which prevents possible downstream merge conflicts. Select `Settings > Actions > General > Workflow permissions > Read and write permissions`. Create a personal access token and add it to the GitHub repository as a secret with the name `RELEASE_TOKEN`.
- Push the local repository to the remote (make sure the development branch is pushed, otherwise the CD pipeline will fail).
- Enable branch protection rules following: TODO: Add reference to steps within this package

## Read the Docs

- [Importing the project to Read the Docs](https://docs.readthedocs.io/en/stable/tutorial/index.html#importing-the-project-to-read-the-docs)
- [Checking the first build](https://docs.readthedocs.io/en/stable/tutorial/index.html#checking-the-first-build)
- [Trigger a build from a pull request](https://docs.readthedocs.io/en/stable/tutorial/index.html#trigger-a-build-from-a-pull-request)

## Package Logo
If you would like to add a logo to your package:
- Add a .png image with the file name `project-sidebar.png` to the /docs/_static directory. Be sure to compress the image.
- Uncomment the block of HTML at the top of the `sidebarintro.html` that enables display of the logo and at line ~154 in `index.html`.
- Commit the changes.

## PyPI

If releasing on PyPI, uncomment the ~lines 25 in `sidebarintro.html` and `sidebarlogo.html`. You may need to update the links contained therein.

## Acknowledgements

This repository is a refactored version of the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
