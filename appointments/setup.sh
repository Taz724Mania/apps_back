#!/usr/bin/env bash

# exit when any command fails
set -o errexit

## Install dependencies via pip
pip install -r ./appointments/dependencies.txt

## Run migration just in case
python manage.py migrate