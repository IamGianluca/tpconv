build:
	poetry install

test:
	pytype tpconv && \
	pytest -s --cov tpconv

pep8_checks:
	flake8 --no-isort-config

format:
	isort -rc -y && \
	black -l 79 .
