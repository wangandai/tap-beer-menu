#!/usr/bin/env bash

pipenv run python telegram_listener.py &>/dev/null &
pipenv run python menu_server.py &>/dev/null &
disown