
sdist: clean
	python3 setup.py sdist

install: sdist
	python3 -m pip install --user dist/pycos-0.0.1.tar.gz

clean:
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf dist
	rm -rf src/pycos.egg-info
	rm -rf tests/__pycache__
