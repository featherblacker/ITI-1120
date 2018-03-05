# Student name: Qiguang Chu
# Student number: # 300042722
# Course: ITI 1120
# Assignment number 2   part 2

import math
###################################################################
# Question 1
###################################################################

def in_or_out_square(a,b,c,d,e):
    '''(int(), int(), int(), int(), int()) -> String()
just calculate if the point is outside the triangle'''
    if c < 0:
        return 'invalid side length'
    elif ((d-a) > 0 and (d-a) < c and (e-b) < c and (e-b) > 0):
        return print("The given query point (",d,", ",e,") is inside of the square.")
    else:
        return print("The given query point (",d,", ",e,") is outside of the square.")

###################################################################
# Question 2
###################################################################

def factorial(n):
    '''int() -> int()
input a integer to get its factorial'''
    m = 1
    while n > 1:
        m = m * n
        n = n - 1
    return m
        
###################################################################
# Question 3
###################################################################

def strange_count(s):
    '''String() -> int()
input a String and count how many characters are in this range '''
    m = len(s)
    n = 0
    for i in s:
        if ((i <= 's') and (i >= 'b')) or ((i >= '3') and (i <= '7')):
            n = n + 1
    print (n)
            
    
###################################################################
# Question 4
###################################################################

def vote_percentage(a):
    '''String() -> double()
input a series of words to count the rate of yes'''
    m = a.count('yes')
    n = a.count('no')
    return m/(n+m)

###################################################################
# Question 5
###################################################################

def vote():
    '''String() -> String()
input a series of words to count the rate of yes and then get
the final result'''
    print("Enter the yes, no, abstained votes one by one and then press enter:")
    s = str(input())
    a = s.count('yes')
    b = s.count('no')
    m = a/(a+b)
    if m == 1:
        print("proposal passes unanimously")
    elif m >= 2/3:
        print("proposal passes with super majority")
    elif m >= 1/2:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")

###################################################################
# Question 6
###################################################################

def alienNumbers(a):
    '''String() -> int()
input characters and count the numbers of each character and
multiply their weight and sum up'''
    t = a.count('T')
    y = a.count('y')
    s = a.count('!')
    b = a.count('a')
    n = a.count('N')
    u = a.count('U')

    sum = t*1024 + y*598 + s*121 + b*42 + n*6 + u
    return sum

###################################################################
# Question 7
###################################################################

def alienNumbersAgain(a):
    '''String() -> int()
add a character at the end as a mark to knonw where to end and
use a circle to get character and do things above'''
    i = 0
    s = 0
    for char in a:
        if char == 'T':
            s = s + 1024
        if char == 'y':
            s = s + 598
        if char == '!':
            s = s + 121
        if char == 'a':
            s = s + 42
        if char == 'N':
            s = s + 6
        if char == 'U':
            s = s + 1
        i = i + 1
    return s

###################################################################
# Question 8
###################################################################

def emphasize(s):
    '''String() -> String()
add a space at each end of character except the last one'''
    a = len(s)
    i = 0
    m = ''
    while i < (a-1):
        m = m + s[i] + ' '
        i = i + 1
    m = m + s[-1]
    return m

###################################################################
# Question 9
###################################################################

def crypto(s):
    '''String() -> String()
split the text up into blocks of two letters each and
swap each pair of letters'''
    a = len(s)
    i = 0
    m = ''
    while i < (a-1):
        m = m + s[i+1] + s[i]
        i = i + 2
    if i%2 == 0:
        m = m + s[-1]
    return m
