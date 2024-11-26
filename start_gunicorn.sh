#!/bin/bash

cd /Users/rdrucker/Documents/match_game/MatchGameInfo/app
source ../mgvenv/bin/activate
gunicorn --reload --workers 3 --capture-output --log-level debug --bind unix:matchgame.sock -m 007 wsgi:app
