# See ../makefile

GIT_CLONE_URL := $(shell git remote get-url --push origin)
CLONE_DIR := 'var/tmp/cloned'

.PHONY: git-init  ## initialize  new git-repo
git-init:
	git init


.PHONY: git-pull  ## git pull
git-pull:
	git pull


.PHONY: git-push  ## git push
git-push:
	git push


.PHONY: git-push-main  ## git-push-main
git-push-main:
	git push -u origin main


.PHONY: git-remote-show-origin  ## git-remote-show-origin
git-remote-show-origin:
	git remote show origin


.PHONY: git-fetch-tags  ## git fetch --tags
git-fetch-tags:
	git fetch --tags


.PHONY: git-show-remote-tags  ## git ls-remote --tags
git-show-remote-tags:
	git ls-remote --tags


.PHONY: git-show-local-tags  ## git tag -l
git-show-local-tags: git-fetch-tags
	echo -e "Local tags"
	git tag -l


.PHONY: git-show-tags  ## show local & remote tags
git-show-tags:
	@echo -e "Local tags"
	git tag -l
	@echo -e "Remote tags"
	git ls-remote --tags


.PHONY: git-ignore-update  ## git-ignore-update
git-ignore-update:
	git rm -r --cached .
	git add .
	git commit -m "Drop files from .gitignore"


.PHONY: git-show-url  ## show clone-url
git-show-url:
	@ git remote get-url --push origin


.PHONY: git-tmp-clone  ## clone repo to tmp-dir
git-tmp-clone:
	LATEST_TAG=$$(git describe --tags --abbrev=0)
	cd ${CLONE_DIR}-${LATEST_TAG}
	@ git clone ${GIT_CLONE_URL} ${CLONE_DIR}


.PHONY: publish-to-pypi  ## publish-to-pypi
publish-to-pypi: git-tmp-clone
	set -e ; \
	LATEST_TAG=$$(git describe --tags --abbrev=0)
	cd ${CLONE_DIR}-${LATEST_TAG} && \
	git fetch --tags && \
	&& \
	git checkout ${LATEST_TAG}
	poetry build && \
	poetry publish