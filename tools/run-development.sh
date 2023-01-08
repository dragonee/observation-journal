#!/bin/sh

set -e

MANAGE_PY=/app/manage.py
REQUIREMENTS=/app/requirements/local.txt
WAIT_FOR=/app/tools/wait-for
DATABASE_HOST=tasks-db:5432

pip3 install -r $REQUIREMENTS

$MANAGE_PY migrate
$MANAGE_PY runserver 0.0.0.0:8000