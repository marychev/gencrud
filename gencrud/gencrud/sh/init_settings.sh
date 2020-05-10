#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

function init_settings() {
  echo_white "Check settings.py file";

  project_name=$1
  SETTINGS_PATH=$PWD"/gencrud/settings.py"

  if test -f $SETTINGS_PATH; then
    echo_purple $SETTINGS_PATH" exist!"
  else
    echo_purple "... start to create settings.py ..." ; sleep 2;
    row="PROJECT_NAME = '$project_name'\nSITE_DOMAIN = '$project_name.com'\nEMAIL_HOST_USER = 'pyapmail@ya.ru'\nEMAIL_HOST_PASSWORD = '${project_name}888'\nDB_NAME = PROJECT_NAME\nDB_USER = DB_NAME\nDB_PASSWORD = '{}888'.format(DB_NAME)\n"
    echo -e $row >> "${PWD}/gencrud/settings.py";
    echo_green "settings.py was created in ${PWD}/gencrud !"
  fi
}