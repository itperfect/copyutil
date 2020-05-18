#!/bin/bash

COUNT=1000


while [ $COUNT -gt 0 ]
do
    SIZE=$(shuf -i 1-1048576 -n 1)

    FILENAMELEN=$((1+RANDOM%15))
    FILEEXTLEN=$((1+RANDOM%4))


    NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w $FILENAMELEN | head -n 1)
    EXT=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w $FILEEXTLEN | head -n 1)


    dd if=/dev/urandom of=/tmp/qwerty/$NAME.$EXT count=1 bs=$SIZE

    (( COUNT-- ))

done