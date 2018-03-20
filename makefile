#!make

init:
	pip install -r requirements.txt
	jupyter labextension install jupyterlab_bokeh

init_dev:
	pip install -r requirements.txt
	pip install -e ./src
	jupyter labextension install jupyterlab_bokeh

build:
	python src/rethinking/tests/compile_example_stan_program.py

format:
	pip install black white
	white $(find -follow | grep '.py$')

test:
	pytest src/
