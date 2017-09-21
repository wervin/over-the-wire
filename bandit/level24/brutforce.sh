#! /bin/bash

for i in {0..99}
do
	((i*=100))
	echo $i
	./script.sh $i &
	sleep 15
done

