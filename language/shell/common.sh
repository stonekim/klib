#!/bin/sh

function pushd_popd_dirs {
   dir=`find . -type d  -maxdepth 1 | tail -1`  
   pushd $dir
   dirs
   popd
}

tar xvfz antiporn_model.tgz -C antiporn --strip-components 1

pushd_popd_dirs
