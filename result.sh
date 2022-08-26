#!/bin/bash
mkdir output
for fullFileName in ./input/*.*
do
	# Get the proposed name by chopping off the extension

     	# get extension.  Set to null when there isn't an extension
     	fileName="${fullFileName##*/}"
			 echo $fileName
     	
	rembg i "${fullFileName}" "./output/${fileName}"
	echo "background removed"
done


echo "hello"
python3 result.py

for fullFileName in ./result/*.*
do
	# Get the proposed name by chopping off the extension

     	# get extension.  Set to null when there isn't an extension
     	fileName="${fullFileName##*/}"
			 echo $fileName
     	
	rembg i "${fullFileName}" "./result/${fileName}"
	echo "background removed"
done
