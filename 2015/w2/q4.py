#!/bin/env python3
import re

data = []
with open("access.log") as f:
    for line in f:
        data.append(line)

byte_input = int(input("Minimum response size: "))

total_requests = 0
total_bytes = 0
for request in data:
    #Date check
    date = re.search("\[(.+)/(.+)/(.+?):.+\]", request)
    if not date: continue
    date = date.groups()
    if int(date[0]) < 1 or int(date[0]) > 9 or date[1] != "Jul" or date[2] != "1995": continue

    #Image check
    http = re.search('\"GET (.+) HTTP/1.0\"', request)
    if not http: continue
    http = http.group(1)
    if http[:7] != "/images" or http[http.rfind(".")+1:].lower() not in ["gif","jpeg","jpg","png"]: continue

    #Http code
    request = request.split(" ")
    if request[-2] != "200": continue

    #Bytes
    if int(request[-1]) >= byte_input:
        total_bytes += int(request[-1])
        total_requests += 1
    
print("# requests: " + str(total_requests))
print("# bytes: " + str(total_bytes))
