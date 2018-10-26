#!/usr/bin/env python3
import os, re, string
uname = re.findall(r"'([^']*)'" , str(os.uname()))
#some regex i found that gets data in quotes from uname
ostype = uname[0]
hostname = uname[1]
ops = re.search(r"[A-Z]+", uname[2])
ops = ops.group()
if uname[-1] == 'x86_64':
    bit = 'x64'
else:
    bit = 'x32'
print(
"""
Live Information---\n
Operating System: %s %s
Host Name: %s
Architecture: %s
""" % (ops, ostype, hostname, bit))
