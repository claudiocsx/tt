clean:
	pip uninstall cs

install:
	pip install -e .['dev']

test:
	pytest tests/ -v --cov=cs
