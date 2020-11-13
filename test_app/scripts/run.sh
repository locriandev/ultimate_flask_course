#!/usr/bin/env bash

export FLASK_DEBUG=1
source virtualenvwrapper.sh
workon flask
flask run
