PYTHON?=python3
ENV?=env
VIRTUALENV?=pyvenv

deps:
	rm -rf $(ENV)
	mkdir -p $(ENV)
	$(VIRTUALENV) $(ENV)
	$(ENV)/bin/python setup.py develop

rmpyc:
	find . -name "*.pyc" -exec rm -rf {} \;

test: rmpyc
	$(ENV)/bin/nosetests simple_midi_parser

.PHONY: deps
