# See ../justfile


# create the virtualenv
[group: 'uv']
uv-create-venv:
	uv venv --seed


# run uv install to create the virtualenv
[group: 'uv']
uv-pip-install:
	uv pip install --editable .


# run uv install without dev-dependencies
[group: 'uv']
uv-pip-install-no-dev:
	uv pip install --no-dev


# run uv sync
[group: 'uv']
uv-sync:
	uv sync


# run uv lock
[group: 'uv']
uv-lock:
	uv lock


# run uv lock --upgrade
[group: 'uv']
uv-lock-upgrade:
	uv lock --upgrade


# run uv build to create the python-package
[group: 'uv']
uv-build:
	uv build --out-dir var/dist


# publish the package to pypi
[group: 'uv']
uv-publish:
	uv publish var/dist/*


# generate a requirements.txt-file
[group: 'uv']
uv-export-requirements:
	uv export --format requirements-txt --output-file requirements.txt


# generate a requirements.txt-file for readthedocs
[group: 'uv']
uv-export-requirements-docs:
	uv export --format requirements-txt --only-group docs --no-hashes --output-file docs/requirements.txt
