#!/bin/bash

CUR_DIR=`pwd`
ISSUE=`cat $CUR_DIR/issue.info`
SUBJECT="update"
[[ -n $1 ]] && SUBJECT=$1

svn ci -m "
TBR=$ISSUE
TBR_REASON=ci_by_tool
TESTED=local
$SUBJECT
"


