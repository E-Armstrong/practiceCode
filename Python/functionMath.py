""" This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three())) """

def zero(x = None):
    if x == None: 
        return 0
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(0 + int(x[0]))
        elif x[1] == '-':
            return int(0 - int(x[0]))
        elif x[1] == 'x':
            return int(0 * int(x[0]))
        elif x[1] == '/':
            return int(0 / int(x[0]))

def one(x = None):
    if x == None:
        return 1
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(1 + int(x[0]))
        elif x[1] == '-':
            return int(1 - int(x[0]))
        elif x[1] == 'x':
            return int(1 * int(x[0]))
        elif x[1] == '/':
            return int(1 / int(x[0]))

def two(x = None):
    if x == None:
        return 2
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(2 + int(x[0]))
        elif x[1] == '-':
            return int(2 - int(x[0]))
        elif x[1] == 'x':
            return int(2 * int(x[0]))
        elif x[1] == '/':
            return int(2 / int(x[0]))

def three(x = None):
    if x == None:
        return 3
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(3 + int(x[0]))
        elif x[1] == '-':
            return int(3 - int(x[0]))
        elif x[1] == 'x':
            return int(3 * int(x[0]))
        elif x[1] == '/':
            return int(3 / int(x[0]))

def four(x = None):
    if x == None:
        return 4
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(4 + int(x[0]))
        elif x[1] == '-':
            return int(4 - int(x[0]))
        elif x[1] == 'x':
            return int(4 * int(x[0]))
        elif x[1] == '/':
            return int(4 / int(x[0]))

def five(x = None):
    if x == None:
        return 5
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(5 + int(x[0]))
        elif x[1] == '-':
            return int(5 - int(x[0]))
        elif x[1] == 'x':
            return int(5 * int(x[0]))
        elif x[1] == '/':
            return int(5 / int(x[0]))

def six(x = None):
    if x == None:
        return 6
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(6 + int(x[0]))
        elif x[1] == '-':
            return int(6 - int(x[0]))
        elif x[1] == 'x':
            return int(6 * int(x[0]))
        elif x[1] == '/':
            return int(6 / int(x[0]))

def seven(x = None): 
    if x == None:
        return 7
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(7 + int(x[0]))
        elif x[1] == '-':
            return int(7 - int(x[0]))
        elif x[1] == 'x':
            return int(7 * int(x[0]))
        elif x[1] == '/':
            return int(7 / int(x[0]))

def eight(x = None):
    if x == None:
        return 8
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(8 + int(x[0]))
        elif x[1] == '-':
            return int(8 - int(x[0]))
        elif x[1] == 'x':
            return int(8 * int(x[0]))
        elif x[1] == '/':
            return int(8 / int(x[0]))

def nine(x = None):
    if x == None:
        return 9
    elif isinstance(x, str): 
        if x[1] == '+':
            return int(9 + int(x[0]))
        elif x[1] == '-':
            return int(9 - int(x[0]))
        elif x[1] == 'x':
            return int(9 * int(x[0]))
        elif x[1] == '/':
            return int(9 / int(x[0]))

def plus(x):
    return str(str(x) + "+")

def minus(x):
    return str(str(x) + "-")

def times(x):
    return str(str(x) + "x")

def divided_by(x):
    return str(str(x) + "/")

Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)