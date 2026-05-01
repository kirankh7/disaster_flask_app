#!/bin/sh
export FLASK_ENV=${FLASK_ENV:-production}
exec gunicorn --bind "0.0.0.0:${PORT:-8000}" --workers 4 --access-logfile - run:app
