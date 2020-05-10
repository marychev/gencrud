#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

function init_sqlite() {
  echo "Try to create migrations and run project";
  run_path=$1
  db_name=$2

  if test -f $PWD/theme/$db_name; then
    echo_purple "File $PWD/theme/$db_name exist!"; sleep 2;
  else
    echo_purple "... start to init project ..." ; sleep 2;
    python $run_path makemigrations
    python $run_path migrate
  fi
}