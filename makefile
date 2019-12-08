format:
	isort -rc -y && \
	black -l 79 .

test:
	pytype tpconv && \
	pytest -s --cov tpconv

format_checks:
	black -l 79 . --check && \
	flake8 --no-isort-config

