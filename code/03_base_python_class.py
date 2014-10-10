"""

====================================================================
                        B A S E   P Y T H O N 
====================================================================

"""

# Questions to get started:
    # Why should data scientists learn to program? 
    # Why learn Python specifically?
    # What is your programming background? In Python? 

# ==================================================================
#                           D A T A  T Y P E S
# ==================================================================

# We'll go over five data types here (all are objects)
# Integer
type(2)
# Float (with the decimal)
type(2.7)
type(2.7e+2)
# Long (more than 10 digits, or L)
type(27L)
# String (either "..." or '...' may be used)
type("Data Science")
type('Data Science')
# Boolean
type(False)

# You can check datatypes
isinstance(1, float)
isinstance(1.0, int)
isinstance(2L, long)
isinstance("Data Science", str)
isinstance(False, bool)

# You can convert between datatypes
int(1.0)
float(1)
int("1")
int(54L)

# ==================================================================
#                           O P E R A T I O N S
# ==================================================================

var1 = 3
var2 = 10

# Boolean Operators
var1 == var2            # EQUAL TO
var1 <  var2            # LESS THAN
var1 <= var2            # LESS THAN OR EQUAL TO        
(var1 == 1) | (var2 == 10)      # OR
(var1 == 1) or (var2 == 10)     # OR (alternative)
(var1 == 1) & (var2 == 10)      # AND
(var1 == 1) and (var2 == 10)    # AND (alternative)

# Addition
10 + 3

# Subtraction
10 - 3

# Multiplication
10 * 3

# Division
10 / 3          # returns 3 in Python 2.x
10 / 3.0        # returns 3.333...
10 / float(3)   # returns 3.333...

# Powers
10**3

# Remainders
10 % 3

# ==================================================================
#           L I S T S :  Mutable, Ordered Data Structures
# ==================================================================

# Lists are denoted by []
lis = [0, 1, 2, 3, 4, 5, 6, 7]
type(lis)

# Specific elemnents can be accessed using [] as well
lis[4] # Returns the 5th element

# Multiple elements can be accessed using the ':' operator
# Returns the 1st number through one shy of the 2nd number
lis[0:4]
# Returns the 5th element through the last element
lis[4:]

# Returns the first through the 4th element
lis[:4]

# Returns the last element
lis[-1]

# Returns the last n elements
lis[-3:]

# List elements are mutable
lis[4] = 100
lis[4:6] = [500, 600]

# The type of list elements is also mutable
lis[0:3] = ["Guido", "Van", "Rossum"]
lis[3:7] = ["created", "python,", "programming", "language,"]

# Check if an element is in a list
"Van" in lis    # returns True

# Elements can be removed with the .remove method
lis.remove(7)

# Elements can be added to the end of a list using the .append method
lis.append("in 1991")

# Elements can be inserted into the middle of a list
lis.insert(5,"a")

# Lists can be nested within each other
# List of three lists
lis = [[1,2,3],[4,5,6],[7,8,9]]

# Lets try to access a particular number, say 6
lis[1][2]

# A list within a list  within a list within a list within a list
lis = [1,2,[3,4,[5,6,[7,8]]]]

# ==================================================================
#      D I C T: Unordered data structures with key-value pairs
#               Keys must be unique
# ==================================================================

dct = {"Name": "Monty Python and the Flying Circus",
       "Description": "British Comedy Group",
       "Known for": ["Irreverant Comedy", "Monty Python and the Holy Grail"],
       "Years Active" : 17,
       "# Members": 6}
       
# Access an element within the list
dct["Years Active"]

# Add a new item to a list within the dictionary
dct["Known for"].append("Influencing SNL")

# Returns the keys
dct.keys()
# Returns the values
dct.values()

# Quiz: Create a dictionary within the 'dct' dictionary containing your
# own favorite Monty Python influences
dct["Influence"] = { "Asteroids": [13681, 9618, 9619, 9620, 9621, 9622], 
                     "Technology": ["Spam", "Python", "IDLE (for Eric Idle)"],
                     "Food": ["Monty Python's Holy Ale", "Vermonty Python"]}

# Accessing a nested dictionary item
dct["Influence"]["Technology"]

# ==================================================================
#                            S T R I N G S
# ==================================================================

# Example strings
s1 = "What is the air-speed velocity"
s2 = "of an unladen swallow?"

# Concatenate two strings
s = s1 + " " + s2
s = " ".join([s1, s2])

# Replace an item within a string
s = s.replace("unladen", "unladen African")

# Return the index of the first instance of a string
s.find("swallow")

# Slice the string
s[-8:]
s[s.find("swallow"):]

# Change to upper and lower case
"swallow".upper()
"SWALLOW".lower()
"swallow".capitalize()

# Count the instances of a substring
s.count(" ")

# Split up a string (returns a list)
s.split()
s.split(" ") # Same thing

# ==================================================================
#                           F U N C T I O N S
# ==================================================================

# Wes McKinney: Functions are the primary and most important method of code
# organization and reuse in Python. There may not be such a thing as too many
# functions. In fact, I would argue that most programmers doing data analysis
# don't write enough functions! (p. 420 of Python for Data Analysis)

# Range returns a list with a defined start/stop point (default start is 0)
range(1, 10, 2) 
range(5, 10) 
range(10)

# Type identifies the object type you pass it
type(3)

# Isinstance checks for the variable type
isinstance(4, str)

# Len returns the length of an object
len("Holy Grail")
len([3, 4, 5, 1])

# User-defined functions start with the 'def' keyword
# They may take inputs as arguments, and may return an output
def my_function(x, y):
    return x - y

# These are equivalent
my_function(100, 10)
my_function(x=100, y=10)
my_function(y=10, x=100)

# This is not equivalent
my_function(10, 100)

# What if we want to make one of our arguments optional?
def my_function_optional(x, y = 10):
    return x - y

# These are equivalent
my_function_optional(100, 10)
my_function_optional(100)

# ==================================================================
#           I F - S T A T E M E N T S   &   L O O P I N G
# ==================================================================

var1 = 10

# If elif else statement
# Whitespace is important
if var1 > 5:
    print "More than 5"
elif var1 < 5:
    print "Less than 5"
else:
    print "5"

# While statement
while var1 < 10:
    print var1
    var1 += 1 # This is commonly used shorthand for var1 = var1 + 1

# For loop
for i in range(0,10,2):
    print i**2

# For loop in the list
fruits = ['apple', 'banana', 'cherry', 'plum']
for i in range(len(fruits)):
    print fruits[i].upper()

# Better way
for fruit in fruits:
    print fruit.upper()

# ==================================================================
#                              I M P O R T
# ==================================================================

# Import a package (collection of (sub)modules)
import sklearn
clf = sklearn.tree.DecisionTreeClassifier()

# Import a specific (sub)module within the sklearn package
from sklearn import tree
clf = tree.DecisionTreeClassifier()

# Import the DecisionTreeClassifer class within the sklearn.tree submodule
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
       
# ==================================================================
#                     L I S T  C O M P R E H E N S I O N
# ==================================================================

# List comprehension is a popular construct in the python programming language:
# Takes an iterable as the input, performs a function on each element of that
# input, and returns a list

# Say you have a list and you want to do something to every element,
# or a subset of this list
numbers = [100, 45, 132.0, 1, 0, 0.3, 0.5, 1, 3]

# Long form using a for loop
lis1 = []
for x in numbers:
    if isinstance(x,int):
        lis1.append(5*x)
        
# Short form using list comprehension
lis2 = [x * 5 for x in numbers if isinstance(x, int)]

# ==================================================================
#                           E X E R C I S E S 
# ==================================================================

# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message


# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]


# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 
#                                       'no', 'Basis', 'for', 'Government']



"""
====================================================================
====================================================================
                    B O N U S   C O N T E N T
====================================================================
====================================================================
"""


# ==================================================================
#           O P T I O N S  F O R  C O D E   E X E C U T I O N
# ==================================================================

"""
Command line
    - Type: 'python myscript.py' to run a script in that directory

Python interpreter
    - Type 'python' into the CLI to enter the interpreter

iPython interpreter
    - Type 'IPython' into the CLI to enter the iPython interpreter
    - Type: run 03_simple.py to run the a script in that directory
    - iPython interpreter has some features, for starters, it looks nicer

iPython Notebook
    - Type 'IPython notebook' into the CLI to open the iPython notebook
    - This is a browser based interpreter that also features in-line plotting
    - Nice as a stand-alone and also for teaching
    - Have heard it doesn't do very well with version control, for that 

Spyder IDE 
    - Nice because allows you to save your code
    - Works nicely with version control
    - Allows you to execute parts of your code

"""

# ==================================================================
#           T H E   W O R K I N G    D I R E C T O R Y
# ==================================================================
import os

# Check the current working directory
os.getcwd()

# Change the current directory
os.chdir('C:\\Python27')

# Change from the current directory
os.chdir('Scripts')

# List out the files in the current directory
for i in os.listdir(os.getcwd()):
    print i

# ==================================================================
#                   D E S I G N  P H I L O S O P H Y
# ==================================================================

import this

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# ==================================================================
#      T U P L E S --> Immutable data structures
# ==================================================================

# Tuples are denoted by ()
tup = ("Monty Python and the Flying Circus", 1969, "British Comedy Group")
type(tup)

# Elements can be accessed in the same way as lists
tup[0]

# You can't change an element within a tuple
tup[0] = "Monty Python"

# Tuples can be "unpacked" by the following
name, year, description = tup

# Tuples can be nested within one another
tup = ("Monty Python and the Flying Circus", (1969, "British Comedy Group"))
