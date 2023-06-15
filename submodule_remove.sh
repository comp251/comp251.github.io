#!/bin/bash

echo "WARNING! This will remove all submodules..."
echo "sleeping for 5 seconds..."

sleep 5

for lab in $(find _labs -type d -depth 1); do 
  printf "removing lab %s...\n" "$lab"
  echo git submodule deinit -f $lab
  echo rm -rf .git/modules/$lab
  echo git rm -f $lab
done
