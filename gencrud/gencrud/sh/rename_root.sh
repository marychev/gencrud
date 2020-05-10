#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

function rename_root() {
  echo_yellow "Attention! This action will rename the root folder."; sleep 1;
  
  OLD_DIR=$PWD
  DIR_TOP="$(dirname ${PWD})";
  DIR_NEW="${DIR_TOP}"/"${1}";
  
  cd ..;
  mv $OLD_DIR $1;  
  cd $1;
  
  echo_green "The root was renamed!"; sleep 1;
}
