# cookiecutter-pylib

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for pure Python libraries.

_As simple as possible. No magic._

## Features

* tox for managing test environments
* pytest for tests
* Sphinx for documentation
* black, flake8 and isort for style checks
* Mypy for type checks

### Missing/Planned

* Automatic selection of Python versions in tox configuration
* License selection
* Versioning (bumpversion? versioneer? setuptools-scm ruled out)
* CI (Azure Pipelines? GitHub Actions?)

## Usage

```
cookiecutter gh:astrojuanlu/cookiecutter-pylib
```

## Alternatives

* https://github.com/ionelmc/cookiecutter-pylibrary, for a more complex setup
* https://github.com/audreyr/cookiecutter-pypackage, more popular but less opinionated
