#!/bin/bash

# Takes every file from the directory, renames each of the .text files to .txt

for file in *;
do 
    if [ ${file: -5 } = ".text" ];
    then
        filename=$(basename -- "$file")
        filename="${filename%.*}"
        printf "$filename\n"

        newfilename="$filename.txt"
        printf "$newfilename\n"

        mv "$file" "$newfilename"
        printf "$file has been renamed to $newfilename\n"

        printf "\n\n"
    fi 
done
