# ty


# show verion of ty
[group: 'ty']
ty-version:
    uv runty --version


# run ty --check on python-files
[group: 'ty']
ty-check args="":
    uv run ty check src/ tests/ {{args}}
