#!/usr/bin/env bash

ps -ef | grep telegram_listener | grep -v grep | awk '{print $2}' | xargs kill
ps -ef | grep menu_server | grep -v grep | awk '{print $2}' | xargs kill