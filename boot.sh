#!/bin/sh
source venv/bin/activate
flask db upgrade
flask  translate compile
gunicorn -b :8000 --access-logfile - --error-logfile - read:read
