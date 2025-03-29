# See ../makefile

# Source .env.template, because .env might not yet exist.
# -include .env.template

# Source .env, if it exists. This Overrides any env-vars sourced in .env.template.
# -include .env


# instantiate the dotenv-file (no override)
# cp --backup  creates .env~, but will overwrite this next time.
# safest way, is to not overwrite existing .env-files, manual intervention needed.
[group: 'dotenv']
dotenv-install-from-template:
	@echo -e "Copying .env.template to .env" ;\
	cp -n .env.template .env ;\
	echo "Please review any credentials in the .env-file."


# replace placeholder __CDW__ with current working directory
[group: 'dotenv']
dotenv-set-basedir:
	@echo -e "Replacing string __CWD__ -> $(PWD)" ;\
	$(SED) -i 's@__CWD__@'"$(PWD)"'@'  .env


# install .env-file from .env.template
[group: 'dotenv']
dotenv-install: dotenv-install-from-template dotenv-set-basedir