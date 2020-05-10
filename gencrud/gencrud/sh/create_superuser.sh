#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

function create_superuser() {
  USER_NAME="admin"
  EMAIL="your-email@mail.com"
  PSW="gencruduser"

  echo_purple "... start to create '${USER_NAME}'"; sleep 1;
  cmd="from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${USER_NAME}', '${EMAIL}', '${PSW}')"
  echo $cmd | python gencrud/manage.py shell
  echo_green "'${USER_NAME}' was created!"; sleep 1;
}
