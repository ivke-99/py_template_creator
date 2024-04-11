#!/usr/bin/env bash
alembic ensure_version
alembic upgrade head
{{cookiecutter.project_name}}