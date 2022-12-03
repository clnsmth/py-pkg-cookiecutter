# {{ cookiecutter.__package_slug }}

{{ cookiecutter.package_short_description }}

## Installation

```bash
pip install git+https://github.com/clnsmth/{{ cookiecutter.__package_slug }}.git#egg={{ cookiecutter.__package_slug }}
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`{{ cookiecutter.__package_slug }}` was created by Colin Smith. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}Colin Smith retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}
