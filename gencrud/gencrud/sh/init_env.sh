#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

function init_env() {
  echo_white "Check environment workspace";

  ENV_PATH=$PWD"/venv/"

  if test -d $ENV_PATH; then
    echo_purple "Environment $ENV_PATH exist!"
    source $ENV_PATHh/bin/activate
  else
    echo_purple "... start to install environment ..." ; sleep 2;
    virtualenv --python=python3 venv
    source $ENV_PATH/bin/activate
    pip install -r $PWD"/gencrud/requirements.txt"
    echo_green "Virtualenv was created!"
  fi
}