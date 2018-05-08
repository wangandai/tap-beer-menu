#!/usr/bin/env bash

pipenv run python3 menu_server.py & sleep 5 &
pipenv run python3 telegram_listener.py &

# disown