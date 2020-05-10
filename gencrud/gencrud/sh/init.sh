#!/bin/bash

read -p "Enter project name: " project_name

if [[ "$PWD" =~ "gencrud" ]]; then
  SH_PATH=$PWD"/gencrud/gencrud/sh/"

  source $SH_PATH"rename_root.sh"
  source $SH_PATH"init_env.sh"
  source $SH_PATH"init_settings.sh"
  source $SH_PATH"init_theme.sh"
  source $SH_PATH"remane_root.sh"

  rename_root $project_name

  RUNSERVER_PATH=$PWD"/gencrud/manage.py"

  init_env
  init_settings $project_name
  init_theme
  init_sqlite $RUNSERVER_PATH $project_name".db"
  create_superuser

  python $RUNSERVER_PATH runserver
fi