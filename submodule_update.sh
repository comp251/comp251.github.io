#!/bin/bash

for lab in $(find _labs -type d); do 
  printf "updating lab %s...\n" "$lab"
  git submodule update --remote --init $lab
done
