#!/bin/bash
#FILES=/path/to/*


for f in `ls -d */`
do
  
  echo "Processing $f file..."

  cp vid.v1.py $f

  cd $f

  python vid.v1.py
  cd ..
  # take action on each file. $f store current file name
  
done
