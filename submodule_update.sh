#!/bin/bash

for lab in $(find _labs -type d -depth 1); do 
  printf "updating lab %s...\n" "$lab"
  git submodule update --remote $lab
done
