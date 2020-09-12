#!/bin/bash
#FILES=/path/to/*
python convertbook.py

for f in `ls -d */`
do
  python convertbook.py
  echo "Processing $f file..."
  cp pdf.py $f
  cp text1.tex $f
  cd $f
  python pdf.py
  cd ..
  # take action on each file. $f store current file name
  
done

bash vidscript.sh
