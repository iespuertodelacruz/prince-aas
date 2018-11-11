#!/bin/bash

cd "$(dirname "$0")"
pipenv run uwsgi --stop /tmp/prince-aas.pid
