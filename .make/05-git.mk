# See ../makefile

.PHONY: git-init  ## initialize  new git-repo
git-init:
	git init


.PHONY: git-pull  ## git pull
git-pull:
	git pull


.PHONY: git-push  ## git push
git-push:
	git push


.PHONY: git-remote-show-origin  ## git-remote-show-origin
git-remote-show-origin:
	git remote show origin


.PHONY: git-ignore-update  ## git-ignore-update
git-ignore-update:
	git rm -r --cached .
	git add .
	git commit -m "Drop files from .gitignore"