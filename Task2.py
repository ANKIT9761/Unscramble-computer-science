
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
dic=dict()
#Adding number,call_duration to dic if not present ,if present adding their calling time to current one
for i in calls:
    if(i[0] not in dic.keys()):
        dic.update({i[0]:int(i[3])})
    if(i[1] not in dic.keys()):
        dic.update({i[1]:int(i[3])})
    else:
        if(i[0] in dic.keys()):
            dic[i[0]]+=int(i[3])
        if(i[1] in dic.keys()):
            dic[i[1]] += int(i[3])
dic=[(k,v) for k,v in sorted(dic.items(),key=lambda x:int(x[1]),reverse=True)]

print(f"{dic[0][0]} spent the longest time,{dic[0][1]} seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#changes are made at line 19
