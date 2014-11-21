#!/bin/bash 
#
# Filename: download_songs.sh
# Author: Justine Lee 
# Date: 10.6.14
# Description: Reads in output file containing SoundCloud urls of cover
# songs, downloads them, and saves them in a subdirectory of the directory
# songs

cd songs

FILE="../cover_urls_lower.txt" 
SC_DOWNLOADER="/Users/justinelee/Projects/Sound-Identification/Soundcloud-Downloader-master/soundcloud-downloader.py"

new_song=true 

while read line; do
	if [ -z "$line" ]; then 
		new_song=true
		cd ..
		continue
	fi

	if [ "$new_song" == true ]; then
		current_song="$line"
		mkdir "$line"
		cd "$line"		
		new_song=false
	else
		python $SC_DOWNLOADER "$line"
	fi


done < "$FILE"
