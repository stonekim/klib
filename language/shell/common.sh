#!/bin/sh

function pushd_popd_dirs {
   dir=`find . -type d  -maxdepth 1 | tail -1`  
   pushd $dir
   dirs
   popd
}


pushd_popd_dirs
