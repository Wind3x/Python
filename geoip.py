#!/usr/bin/python

# Simple script to get GeoIP information on a set of IPv4 addresses
# Accepts a dataset with headers where the IPs are in the first column
#  and rows are separated by newlines
# Prints the dataset with additiional columns for country code and name per IP
#  and is currently set to filter out US United States IPs
import GeoIP

f = open('full.txt', 'r')
data = []
for line in f:
  data.append(line.split())
 
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

for x in range(len(data)):
  if data[x]:
    if x != 0: #not headers
      data[x].append(gi.country_code_by_addr(data[x][0]))
      data[x].append(gi.country_name_by_addr(data[x][0]))
    else:
      data[x].append('country_code')
      data[x].append('country_name')
    if not 'US' in data[x]:
      s = ''
      for y in range(len(data[x])):
        if data[x][y]:
          s += (str(data[x][y]) + '\t')
      print(s)
