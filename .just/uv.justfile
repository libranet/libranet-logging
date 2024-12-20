# uv / venv


# create .env from .env.template
[group: 'venv']
install-dotenv:
    @ echo -e "Copying .env.template to .env" ;
    @ cp -n .env.template .env ;
    @ echo "Please review the config in .env"
    @ echo -e "Replacing string __CWD__ -> $(pwd)"
    @ sed -i 's@__CWD__@'"$(pwd)"'@' .env


# run all install-steps to full initial installation
[group: 'venv']
install: create-dirs uv-sync symlink-venv-dirs install-dotenv


# create files and directories
[group: 'venv']
create-dirs:
	@ mkdir -p var/cache
	@ mkdir -p var/docs/
	@ mkdir -p var/log/sphinx
	@ mkdir -p var/tmp


# symlink venv-dirs to make bin/python work
[group: 'venv']
symlink-venv-dirs:
	@ ln -sf .venv/bin
	@ ln -sf .venv/lib
	@ ln -sf .venv/lib64
	@ ln -sf .venv/pyvenv.cfg


# upgrade uv itself
[group: 'uv']
upgrade-uv:
	uv self update



# install the project and all dependencies from the default groups
[group: 'uv']
uv-sync:
    unset VIRTUAL_ENV
    uv sync

alias uv-install := uv-sync
alias create-venv := uv-sync


# update uv.lock
[group: 'uv']
uv-lock:
    unset VIRTUAL_ENV
    uv lock


# build the python-package
[group: 'uv']
uv-build:
    unset VIRTUAL_ENV
    uv build


# publish the python-package
[group: 'uv']
uv-publish:
    uv publish dist/* --verbose


# publish the python-package
[group: 'uv']
uv-build-and-publish: uv-sync uv-build uv-publish


# export uv-defined requirements to a pip-installable requirements-file
[group: 'uv']
[unix]
uv-export-requirements:
    @ uv export --format requirements-txt --no-hashes --output-file etc/pip/requirements.txt
    @ cat etc/pip/requirements-header.txt <(echo "") etc/pip/requirements.txt > etc/pip/temp.txt && mv etc/pip/temp.txt etc/pip/requirements.txt
    @ echo -e "Updated etc/pip/requirements.txt"


# export uv-defined requirements to a pip-installable requirements-file
[group: 'uv']
[windows]
uv-export-requirements:
    Get-Content etc/pip/requirements-header.txt | Set-Content etc/pip/temp.txt
    Add-Content -Path etc/pip/temp.txt -Value ""
    Get-Content etc/pip/requirements.txt | Add-Content -Path etc/pip/temp.txt
    Move-Item etc/pip/temp.txt etc/pip/requirements.txt -Force

alias uv-export := uv-export-requirements