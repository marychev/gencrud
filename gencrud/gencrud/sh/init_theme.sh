#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"
source $SH_PATH"init_app.sh"
source $SH_PATH"init_db.sh"
source $SH_PATH"create_superuser.sh"

function init_theme() {
  init_app

  echo "Check theme workspace:";

  theme_path=$PWD"/theme/"
  zip_path=$PWD"/gencrud/gen/theme.zip"

  if test -d $theme_path; then
    echo_purple "Theme ${theme_path} exist!"
  else
    echo_purple "... start to unzip archive ..." ; sleep 2;
    unzip $zip_path -d $PWD
    echo_green "Theme was created! ${theme_path}"
  fi
}