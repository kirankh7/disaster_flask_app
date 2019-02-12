#!/bin/sh

GUNICORN=/usr/local/bin/gunicorn
ROOT=/var/flask_app/disaster_flask_app
PID=/var/run/gunicorn.pid

APP=app:app

if [ -f $PID ]; then rm $PID; fi

cd $ROOT
exec $GUNICORN -c $ROOT/app.py --pid=$PID $APP
