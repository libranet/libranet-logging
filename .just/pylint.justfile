# See ../justfile


# show which pylint is used
[group: 'pylint']
pylint-which:
	@ which pylint


# run pylint on python-files
[group: 'pylint']
pylint: pylint-which
	- pylint src/ tests/
