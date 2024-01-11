package := aioretry1
sources := $(wildcard $(package)/*.py)

test:
	python3 tests.py

dist: setup.py test
	rm -f dist/*
	python3 $< sdist

publish: dist
	twine upload dist/*

.PHONY += test dist publish
