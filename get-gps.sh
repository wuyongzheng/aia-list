#!/bin/bash

for p in `grep PARSE_RESULT pass3.txt | cut -f 6 | grep 'SINGAPORE [0-9]*$' | sed -e 's/.*SINGAPORE //' | sort -u` ; do
	wget -O - "https://www.google.com.sg/maps/place/Singapore+$p/" | grep -m 1 "\"Singapore $p\",\[" | sed -e "s/.*\"Singapore $p\",\[\([0-9]*.[0-9]*\),\([0-9]*.[0-9]*\)\].*/$p \1 \2/"
	sleep 1
done
