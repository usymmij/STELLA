#! /bin/bash

# usage
# . com.sh usymmij \<usymmij@gmail.com\> 1/30/2025 "20:19:19 EST"

GIT_COMMITTER_NAME=$1
GIT_COMMITTER_EMAIL=$2
GIT_AUTHOR_DATE=$(date -d$3)
GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"

git commit --author="$1 $2" --date="$GIT_AUTHOR_DATE $4"

