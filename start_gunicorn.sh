#!/bin/bash

cd /Users/milesdame/Documents/dolphin/app
source ../.venv/bin/activate
gunicorn --reload --workers 3 --capture-output --log-level debug --bind unix:dolpin.sock -m 007 wsgi:app
