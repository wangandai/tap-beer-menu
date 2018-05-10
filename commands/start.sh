#!/usr/bin/env bash

nohup pipenv run python3 menu_server.py & disown
sleep 15
nohup pipenv run python3 telegram_listener.py & disown