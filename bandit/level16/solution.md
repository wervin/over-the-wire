nmap -v -p31000-32000 localhost

31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

openssl s_client -ign_eof -connect localhost:31790 < /etc/bandit_pass/bandit16
