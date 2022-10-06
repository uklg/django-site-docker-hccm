#!/bin/bash
set -x
/code/manage.py makemigrations
/code/manage.py migrate
/code/expect
#/code/expect;/code/manage.py runserver 0.0.0.0:8000
