#!/usr/bin/env bash

pipenv run python3 telegram_listener.py &
pipenv run python3 menu_server.py &
# disown