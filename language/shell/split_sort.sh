#!/bin/bash
lines=$(wc -l $1 | sed 's/ .*//g')
lines_per_file=`expr $lines / 20`
split -d -l $lines_per_file $1 __part_$1
for file in __part_*
do
{
  sort $file > sort_$file
} &
done
wait
sort -smu sort_* > $2
rm -f __part_*
rm -f sort_*
