'''
SOLUTIONS: Base Python Exercises
'''


'''
Exercise 1:
Create a calculator function. If the operation is not specified,
default to addition. If the operation is invalid, print an error message.
'''

from __future__ import division

def my_calc(a, b, op='add'):
    if op == 'multiply':
        return a*b
    elif op == 'divide':
        return a/b
    elif op == 'add':
        return a+b
    elif op == 'subtract':
        return a-b
    else:
        print 'error: valid operations are add, subtract, multiply, divide'

my_calc(5, 6)
my_calc(5, 6, 'add')
my_calc(5, 6, 'subtract')
my_calc(5, 6, 'divide')
my_calc(5, 6, 'multiply')
my_calc(5, 6, 'other')


'''
Exercise 2:
Given a list of numbers, return a list where ADJACENT duplicate elements
have been reduced to a single element.
'''

def remove_adjacent_dupes(original_list):
    new_list = []
    new_list.append(original_list[0])
    for num in original_list[1:]:
        if num != new_list[-1]:
            new_list.append(num)
    return new_list

def remove_adjacent_dupes(original_list):
    new_list = []
    for num in original_list:
        if len(new_list) == 0 or num != new_list[-1]:
            new_list.append(num)
    return new_list

def remove_adjacent_dupes(original_list):
    i = len(original_list) - 1
    while i > 0:
        if original_list[i] == original_list[i-1]:
            del original_list[i]
        i -= 1
    return original_list

remove_adjacent_dupes([1, 2, 2, 3])
remove_adjacent_dupes([1, 2, 3])
remove_adjacent_dupes([1, 2, 2, 3, 2])
remove_adjacent_dupes([1, 1, 2, 3, 2])


'''
Exercise 2 Bonus:
Given a list of numbers, return a list where ALL duplicate elements
have been reduced to a single element.
'''

def remove_dupes(original_list):
    new_list = []
    for num in original_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

def remove_dupes(original_list):
    sorted_list = sorted(original_list)
    new_list = []
    for num in sorted_list:
        if len(new_list) == 0 or num != new_list[-1]:
            new_list.append(num)
    return new_list

def remove_dupes(original_list):
    return(list(set(original_list)))

remove_dupes([1, 2, 2, 3])
remove_dupes([1, 2, 3])
remove_dupes([1, 2, 2, 3, 2])
remove_dupes([1, 1, 2, 3, 2])


'''
Exercise 3:
Given a string, convert it to a list of words, capitalize all words that
are more than 3 characters long, and DISCARD the other words.
'''

quote = "Strange women lying in ponds is no basis for government"
[word.capitalize() for word in quote.split() if len(word) > 3]


'''
Exercise 3 Bonus:
Given a string, convert it to a list of words, capitalize all words that
are more than 3 characters long, and KEEP the other words.
'''

quote = "Strange women lying in ponds is no basis for government"
[word.capitalize() if len(word) > 3 else word for word in quote.split()]
