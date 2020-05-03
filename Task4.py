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
a=[i[0] for i in calls]
a=set(a)

for i in calls:
    if(i[1] in a):
        a.remove(i[1])
for i in texts:
    if(i[0] in a):
        a.remove(i[0])
    if(i[1] in a):
        a.remove(i[1])
a=sorted(a)

print("These numbers could be telemarketers: ",*a,sep='\n')

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

