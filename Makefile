# This is a comment.
# You *must* indent using <TAB>s, not spaces.
# For the complete Reference, please see https://www.gnu.org/software/make/manual/make.html
# Commands starting with "-" are ignoring their exit-code.

# If you're using GNU make and you need help debugging a makefile then there
# is a single line your should add. And it's so useful that you should add it
# to every makefile you create.
# cfr. http://blog.jgc.org/2015/04/the-one-line-you-should-add-to-every.html
print-%: ; @echo $*=$($*)


# notdir: Extracts all but the directory-part of each filename.
# cfr https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html
PACKAGENAME = $(notdir $(CURDIR))

# For ENVNAME, we assume the package-code is located in a 'src'-subdirectory of the virtualenv.
ENVNAME = $(notdir $(realpath $(CURDIR)/../.. ))


# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .


clean:
	- rm -f MANIFEST
	- rm -rf dist/
	- rm -fr docs/_build
	- rm -fr htmlcov/
	@rm -rf build dist *.egg-info
	@find . -name '*.py?' -delete

develop:
	# install this package in develop-mode
	python setup.py develop

flake8:
	- flake8 src/$(PACKAGENAME)

isort:
	- isort **/*.py

pytest:
	- py.test

pytest-pdb:
	- py.test --pdb

pytest-cov:
	- py.test --cov=$(PACKAGENAME) --cov-report html -v tests/

pytest-pdb-cov:
	- py.test --cov=$(PACKAGENAME) --cov-report html -v tests/  --pdb

pytest-pdb-cov-lf:
	- py.test --cov=$(PACKAGENAME) --cov-report html -v tests/  --pdb --lf

copy-cov:
	- rm -fr /var/www/html/docs/$(PACKAGENAME)-coverage/*
	- cp -r htmlcov/*  /var/www/html/docs/$(PACKAGENAME)-coverage/
	# - scp -r htmlcov/* example.com:/var/www/html/docs/$(PACKAGENAME)-coverage/


sphinx-docs:
	cd docs && $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html && cd ..
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
