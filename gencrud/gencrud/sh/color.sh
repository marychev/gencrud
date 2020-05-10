#!/bin/bash

BLACK='\033[0;30m'
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'

function echo_red() { echo -e "${RED}$1${WHITE}"; }
function echo_green() { echo -e "${GREEN}$1${WHITE}"; }
function echo_purple() { echo -e "${PURPLE}$1${WHITE}"; }
function echo_yellow() { echo -e "${YELLOW}$1${WHITE}"; }
function echo_white() { echo -e "${WHITE}$1${WHITE}"; }