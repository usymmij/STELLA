#! /bin/bash

NAMES=$(git shortlog -sne | awk -F" " '{print $NF}' | awk '!seen[$NF]++')
for name in $NAMES
do

  echo $name

  echo $(echo usymmij
  git log --shortstat --author="$name" | grep -E "fil(e|es) changed" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print "files changed: ", files, "lines inserted: ", inserted, "lines deleted: ", deleted }')
  echo 
done

