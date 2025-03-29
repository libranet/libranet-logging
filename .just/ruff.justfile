# See ../justfile


# show which ruff is used
[group: 'ruff']
ruff-which:
	@ which ruff


# run ruff on python-files
[group: 'ruff']
ruff:
	- ruff docs/ src/ tests/


# run ruff --check on python-files
[group: 'ruff']
ruff-check:
	- ruff check docs/ src/ tests/


# run ruff --fix on python-files
[group: 'ruff']
ruff-fix:
	- ruff --fix docs/ src/ tests/