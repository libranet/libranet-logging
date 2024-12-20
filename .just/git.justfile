# git


# list all git-tags
[group: 'git']
git-tag-list:
    git tag --list


[group: 'git']
git-tag-list-versions nr="3":
    @ echo -e "Latest tagged versions:"
    @ git tag --list --sort=-v:refname | grep -P '^\d+\.\d+(\.\d+)?$'| head -{{nr}}


# delete a tags locally + remote
[group: 'git']
git-remove-tag tag:
    git tag -d {{tag}}
    git push --delete origin {{tag}}


# create a new tag and push it to remote
[group: 'git']
git-tag-new tag:
    git tag {{tag}}
    git push --tags


# run git maintenance
[group: 'git']
git-maintenance-run:
    git maintenance run


# start git maintenance
[group: 'git']
git-maintenance-start:
    git maintenance start


# stop git maintenance
[group: 'git']
git-maintenance-stop:
    git maintenance stop


[group: 'git']
[unix]
git-check-uncommitted-changes:
    #!/usr/bin/env bash
    # set -euxo pipefail
    set -euo pipefail

    # Check if there are any uncommitted changes
    if [[ $(git status --porcelain) ]]; then
        echo "There are uncommitted changes:"
        git status --short
        exit 1
    else
        echo "All files are committed."
        exit 0
    fi
