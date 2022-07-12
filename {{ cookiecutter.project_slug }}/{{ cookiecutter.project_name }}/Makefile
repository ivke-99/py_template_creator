SHELL := /bin/bash
env:
	pip install -r requirements/test.txt  > /dev/null

run:
	@echo "Running service..."
	. ../env.sh && \
	python {{cookiecutter.app_name}}/run.py
test:
	@echo "Running unit tests..."
	. ../env.sh && \
	env TEST_DB=True coverage run --source={{cookiecutter.app_name}} setup.py test ${module} && \
	coverage html && \
	coverage report
	@echo
	@echo "Flake8 errors in code ----------------"
	@echo
	@echo "--------------------------------------"
	@python -m flake8 --max-line-length=180 --exclude .git,__pycache__,.eggs,build
	@echo "OK, no flake8 errors in code"
	@echo "--------------------------------------"

lint:
	@python -m flake8 --max-line-length=180 --exclude .git,__pycache__,.eggs,build
migrate:
	@echo "Running migrations ..."
	. ../env.sh && \
	python {{cookiecutter.app_name}}/migrations/manage.py upgrade
	@echo "Migrations finished."

downgrade:
	@echo "Running migrations ..."
	. ../env.sh && \
	python {{cookiecutter.app_name}}/migrations/manage.py downgrade ${level}
	@echo "Migrations finished."

init_db:
	@echo "Running migrations ..."
	. ../env.sh && \
	python {{cookiecutter.app_name}}/migrations/manage.py version_control
	@echo "Migrations finished."
