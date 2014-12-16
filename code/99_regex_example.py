'''
CLASS: Regular Expressions Example
'''


'''
Open file
'''

# open file and store each line as one row
with open('../data/homicides.txt', 'rU') as f:
    raw = [row for row in f]


'''
Create a list of ages 
'''

import re

ages = []
for row in raw:
    match = re.search(r'\d+ years old', row)
    if match:
        ages.append(match.group())
    else:
        ages.append('0')

ages = [int(element.split()[0]) for element in ages]

# simplify process using a lookahead
ages = []
for row in raw:
    match = re.search(r'\d+(?= years)', row)
    if match:
        ages.append(int(match.group()))
    else:
        ages.append(0)


'''
Create a list of causes
'''

causes = []
for row in raw:
    match = re.search(r'Cause: .+?<', row)
    if match:
        causes.append(match.group())
    else:
        causes.append('Cause: unknown<')

causes = [element[7:-1] for element in causes]

# simplify process using a lookahead and a lookbehind
causes = []
for row in raw:
    match = re.search(r'(?<=Cause: ).+?(?=<)', row)
    if match:
        causes.append(match.group())
    else:
        causes.append('unknown')


'''
Generate simple statistics
'''

from collections import Counter

c_ages = Counter(ages)
sum(c_ages.values())    # 1250
c_ages[0]               # 22

c_causes = Counter(causes)
sum(c_causes.values())  # 1250
c_causes.most_common()
