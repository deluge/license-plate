help:
	@echo "devinstall - install all packages required for development"
	@echo "correct - Format python code by isort and black"
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"
	@echo "i18n - process py related i18n files"
	@echo "compilei18n - generate compiled gettext catalogs"

devinstall:
	pip install --upgrade pip setuptools wheel poetry
	poetry install
	sh -c 'if [ ! -f src/app/settings.py ]; then echo "from app.conf.dev_settings import *" > src/app/settings.py; fi'

correct:
	isort .
	black .

tests:
	py.test --isort --flake8 ${ARGS}

coverage:
	py.test --cov ${ARGS}

coverage-html:
	py.test --cov --cov-report=html ${ARGS}

i18n:
	python src/manage.py makemessages -i htmlcov -i web -i migrations -v2 -l de

compilei18n:
	python src/manage.py compilemessages -v2
