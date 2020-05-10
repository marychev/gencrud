#!/bin/bash

echo "RESTORE DB: >>> $(pwd) <<<"

path="$HOME/project/gencrud_web/"
source $path.gencrud/gencrud/sh/color.sh

user=$(whoami)
dbname="homebio"
dbuser="homebio"
dbpsw="homebio888"
path_backup=$path"theme/"
dbfilename="backup.sql"

echo "Home: $HOME | User: $user | DBName: $dbname | DBUser: $dbuser"
echo -e "List backups: "; find $path_backup -name *.sql;

sleep 1; echo -e "${YELLOW}
# -- USE THIS ----------------------------------- #
drop database $dbname; create database $dbname; \q
# ----------------------------------------------- #${WHITE}"; 
sudo -u postgres psql

sleep 2
echo -e "NOW START BACKUP: # ${BLACK}$dbpsw${WHITE}"
psql -h localhost -U $dbuser -d $dbname -f $path_backup$dbfilename;
echo -e "${GREEN}\r\n\tDATABASE $dbname UPDATED!"