#! /bin/bash

filename="data"
gzip=".gz"
tar=".tar"
bzip=".bz"
buf=""

xxd -r $1 $filename

while true
do
	mv data* $filename

	if [ $(file $filename | grep -o 'gzip') ];
	then
		buf=$filename$gzip
		mv $filename $buf
		gzip -dvf $buf  
		continue
	fi

	if [ $(file $filename | grep -o 'bzip') ];
	then
		buf=$filename$bzip
		mv $filename $buf
		bzip2 -dvf $buf
		continue
	fi

	if [ $(file $filename | grep -o 'tar') ];
	then
		buf=$filename$tar
		mv $filename $buf
		tar -xvf $buf	
		rm $buf
		continue
	fi
	
	break

done
exit 0

