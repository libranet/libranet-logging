# See ../justfile


# symlink bin/ipython to bin/ip
[group: 'ipython']
ipython-symlink-to-ip:
	- cd .venv/bin && ln -sf ipython ip && cd -
