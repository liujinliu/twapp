all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr */*.egg-info build dist

build: clean
	python setup.py build_py bdist_wheel
	cp Makefile dist

install: build
	pip install dist/*.whl -U

deploy:
	pip install *.whl -U


.PHONY : all clean build install
