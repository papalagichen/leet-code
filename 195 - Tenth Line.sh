#!/usr/bin/env bash

i=1

while read line; do
    if [ $i -eq 10 ]; then
        echo $line
        break
    else
        i=$((i + 1))
    fi
done < file-195.txt
