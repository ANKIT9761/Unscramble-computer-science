"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
count=[]
for _ in texts:
    if(_[0] not in count):
        count.append(_[0])
    if(_[1] not in count):
        count.append(_[1])
for i in calls:
    if (i[0] not in count):
        count.append(i[0])
    if (i[1] not in count):
        count.append(i[1])
print(f"There are {len(count)} different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
