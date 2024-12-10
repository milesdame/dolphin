#!/bin/bash

cd /Users/rdrucker/Documents/dolphin/app
source ../mgvenv/bin/activate
gunicorn --reload --workers 3 --capture-output --log-level debug --bind unix:dolphin.sock -m 007 wsgi:app
