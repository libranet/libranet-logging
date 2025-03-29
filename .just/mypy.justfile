# See ../justfile

# show which mypy is used
[group: 'mypy']
mypy-which:
	@ which mypy


# run mypy on python-files
[group: 'mypy']
mypy: mypy-which
	mypy src tests

# run mypy with html-reporting
[group: 'mypy']
mypy-report: mypy-which
	mypy src tests --html-report  var/coverage-mypy/