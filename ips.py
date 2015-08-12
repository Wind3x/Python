#!/usr/bin/python

import re

#lines.out = output of all lines containing IP addresses
#ips.out = output of all IP addresses in the input file

#Regex for IPv4 address
r = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'

#Read in a file
infile = raw_input('input --> ')
f = open(infile, 'r')

ips = []

lines = f.readlines()

#Creates a list of lines containing IP addresses
for line in lines:
    m = re.search(r, line)
    if m:
        ips.append(line)

ips = set(ips)
ips = sorted(ips)

name1 = infile + '.lines.out'
outfile = open(name1, 'w')
for line in ips:
        outfile.write(str(line) + '\n')

#Creates a list only containing IPs
only = []
for item in ips:
    only.append(re.findall(r, item))

dedup = []
for item in only:
        if len(item) > 1:
                for i in item:
                        dedup.append(i)
        else:
                dedup.append(item[0])

dedup = set(dedup)
dedup = sorted(dedup)

name2 = infile + '.ips.out'
outfile2 = file(name2, 'w')
for item in dedup:
        outfile2.write(str(item) + '\n')
