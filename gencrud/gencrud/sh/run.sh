#!/bin/bash

source $PWD"/gencrud/gencrud/sh/color.sh"
source venv/bin/activate

RUNSERVER_PATH=$PWD'/gencrud/manage.py'

if test -f $RUNSERVER_PATH; then
  echo_green "Project ${path} RUN! http://localhost:8000/"
  python $RUNSERVER_PATH runserver
 else
  	echo_red "File doesn't found"
fi
