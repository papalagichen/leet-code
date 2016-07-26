#!/usr/bin/env bash

while read -a line; do
    for ((i=0; i < "${#line[@]}"; i++)); do
        a[$i]="${a[$i]} ${line[$i]}"
    done
done < file-194.txt

for ((i=0; i < ${#a[@]}; i++)); do
    echo ${a[i]}
done
