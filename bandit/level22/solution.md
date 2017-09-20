# ouvrir une première session persistante
ssh -l bandit22 -p 2220 -L 1234:localhost:22 bandit.labs.overthewire.org
# ouvrir une deuxième session
ssh -p 1234 bandit23@localhost
# dans la première session
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
