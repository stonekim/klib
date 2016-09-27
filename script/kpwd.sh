#!/bin/bash

protocol=$1
file=$2
path=`pwd`
optional=

SUPPORT_PROT='wget ftp scp'

file_path="$path/$file"

[[ -d $file_path ]] && optional="$optional -r"

case $protocol  in
    'wget')
        [[ -d $file_path ]] && optional="$optional --cut-dir=`echo $path | awk -F '/' '{print NF-2}'`"
        echo "wget $optional ftp://${HOSTNAME}$file_path"
     ;;

    'scp')
        echo "scp $optional ${USER}@$HOSTNAME:$file_path ."
    ;;
    '*')
        echo "ftp://${HOSTNAME}$file_path"
    ;;
esac
    

