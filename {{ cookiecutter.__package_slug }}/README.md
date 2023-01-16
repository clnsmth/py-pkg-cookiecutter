[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![Actions Status: CI/CD]([https://github.com/clnsmth/{{ cookiecutter.__package_slug }}/workflows/ci-cd/badge.svg)](https://github.com/clnsmth/{{ cookiecutter.__package_slug }}/actions/workflows/ci-cd.yml](https://github.com/clnsmth/{{ cookiecutter.__package_slug }}/actions/workflows/ci-cd.yml))
[![codecov.io](https://codecov.io/gh/clnsmth/{{ cookiecutter.__package_slug }}/branch/main/graph/badge.svg)](https://codecov.io/github/clnsmth/{{ cookiecutter.__package_slug }}?branch=main)

# {{ cookiecutter.__package_slug }}

{{ cookiecutter.package_short_description }}

_TODO: Describe the context/motivation for this package._

## Quick Start

Install the current release from GitHub.

```bash
pip install git+https://github.com/clnsmth/{{ cookiecutter.__package_slug }}.git#egg={{ cookiecutter.__package_slug }}
```

_TODO: Include brief demonstration of how to use this package._

## Documentation

The official documentation is hosted on ReadTheDocs: https://github.com/clnsmth/{{ cookiecutter.__package_slug }}

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`{{ cookiecutter.__package_slug }}` was created by Colin Smith. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}Colin Smith retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}
