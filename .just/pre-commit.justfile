# See ../makefile


# show which pre-commit is used
[group: 'pre-commit']
pre-commit-which:
	@ which pre-commit


# install the pre-commit-hook in .git/hooks
[group: 'pre-commit']
precommit-install-hook:
	pre-commit install


# run all precommit-steps on all files
[group: 'pre-commit']
precommit-run-files:
	pre-commit run --all-files
