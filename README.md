# Yeti-web Admin API SDK
![tests workflow](https://github.com/yeti-switch/yeti-switch-api-python/actions/workflows/tests.yml/badge.svg)

The documentation for the Yeti-web Admin API can be found [here](https://yeti-switch.org/docs/en/admin-api/index.html).

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.
```shell
pip3 install yeti-switch-api
```

Or download source code and run:
```shell
python3 setup.py install
```

## Usage

```python

import yeti_switch_api

yeti_switch_api.orm.OrmClient({
    'API_ROOT': 'https://myhost.com/api/rest/admin',
    'AUTH_CREDS': {
        'login': 'mylogin',
        'password': 'mypassword',
    },
    'VALIDATE_SSL': True,
    'TIMEOUT': 10,
})

# refresh auth token in any time
yeti_switch_api.orm.OrmClient.auth.refresh_token()

# use the api
found_contractors = yeti_switch_api.orm.Contractor.get_list()
```

See `examples/` for detailed usage examples.

## Development

### Requirements

[pipenv](https://pipenv.pypa.io/en/latest/) can be installed via `apt install pipenv`

`Python 3.7+`

### Install dependencies

```shell
pipenv install --dev
```

### Lint with flake8
```shell
pipenv run python -m flake8 . --count --show-source --statistics
```

### Fix code format with Black
```shell
pipenv run python -m black .
```

## Release

### Change `__version_info__` in `yeti_switch_api/__init__.py`

### Build package
```shell
pipenv run python setup.py sdist
pipenv run python setup.py bdist_wheel
```
As result you will have files:
```
dist/yeti_switch_api-<VERSION>.tar.gz
dist/yeti_switch_api-<VERSION>-py3-none-any.whl
```

### Check package
```shell
pipenv run python -m twine check dist/*
```

### Upload package to [pypi](https://pypi.org/)

```shell
pipenv run python -m twine upload dist/*
```

**Notes:** see [this guide](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#create-an-account) how to set up pypi account

### Upload package to test pypi
```shell
pipenv run python -m twine upload -r testpypi dist/*
```
