# See ../justfile


# initialize  new git-repo
[group: 'git']
git-init:
	git init


# git-remote-show-origin
[group: 'git']
git-remote-show-origin:
	git remote show origin


# git fetch --tags
[group: 'git']
git-fetch-tags:
	git fetch --tags


# git ls-remote --tags
[group: 'git']
git-show-remote-tags:
	git ls-remote --tags


# git tag -l
[group: 'git']
git-show-local-tags: git-fetch-tags
	echo -e "Local tags"
	git tag -l


# show local & remote tags
[group: 'git']
git-show-tags:
	@echo -e "Local tags"
	git tag -l
	@echo -e "Remote tags"
	git ls-remote --tags
