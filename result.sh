#!/bin/bash
for fullFileName in ./input/*.*
do
	# Get the proposed name by chopping off the extension

     	# get extension.  Set to null when there isn't an extension
     	fileName="${fullFileName##*/}"
     	
	backgroundremover -i "${fullFileName}" -o "./output/${fileName}"
	echo "background removed"
done


echo "hello"
python3 1.py
