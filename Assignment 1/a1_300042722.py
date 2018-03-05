# Student name: Qiguang Chu
# Student number:  300042722
# Course: IT1 1120 
# Assignment Number 1

import turtle
import math


##################################################################
# Question 1
###################################################################
def lbs2kg(w):
    ''' (number) -> (number)
    Returns the weight w expressed in pounds as killograms'''
    weight = w*0.45359237
    return weight
    

###################################################################
# Question 2
###################################################################
def id_formater(fn, ln, appelation, city, year):
    ''' (str) -> (str)
    Return the string of form “appelation. ln,fn (city, year)'''
    
    return str(appelation + '. ' + ln + ', ' + fn + ' ' +'('+city+', '+ str(year) +')')
    

###################################################################
# Question 3
###################################################################
def id_formater_display():
    '''Print questions and then get input from users'''
    print('What is your first name? ', end="")
    fn = input()
    print('What is your last name? ', end="")
    ln = input()
    print('What is your appellation? ', end="")
    appelation = input()
    print('Where were you born? ', end="")
    city = input()
    print('What is your year of birth? ', end="")
    year = input()
    print('\n')
    '''print user's ID'''
    print(id_formater(fn, ln, appelation, city, year))


###################################################################
# Question 4
###################################################################
def l2loz(w):
    '''(int) -> ((int), (int))
    take the interger down to floor and then get the remain'''
    l = math.floor(w)
    o = (w - l)*16
    return (l, o)


##################################################################
# Question 5
###################################################################
def median3(num1,num2,num3):
    '''((int), (int), (int)) -> (string)
    compare these three numbers and conclude which is(are) the miedium number'''
    print(str(num1) + " is a median. That is " + str(bool((num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3))))
    print(str(num2) + " is a median. That is " + str(bool((num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3))))
    print(str(num3) + " is a median. That is " + str(bool((num3 >= num1 and num3 <= num2) or (num3 <= num1 and num3 >= num2))))
    

##################################################################
# Question 6
###################################################################
def forms_triangle(a, b, c):    
    ''' (int) -> (bool)
    just let each side to be less than the sum of the other two sides'''
    return (bool((a < b + c) and (b < a + c) and (c < a + b)))

###################################################################
# Question 7
###################################################################
def below_parabola(a,b,p,q):
    '''(int) -> (bool)
    For points which are below or on the curve, return true
    and for others, return false'''
    y = a*p**2 + b
    return (bool(q <= y))


###################################################################
# Question 8
###################################################################
def efun(x):
    '''(int) -> (int)
    calculate y by using the equation below'''
    y = math.log(x+2)/17
    return y


###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name):
    '''(string) -> (string)
    calculate numbers of stars and space and print in order'''
    title = "__" + name +"__"
    stars = len(title) + 6
    print('*'* stars)
    print('*' + ' '*(stars-2) +'*')
    print('*' + ' '*(stars-2) +'*')
    print('*' + ' '*2 + title + ' '*2 +'*')
    print('*' + ' '*(stars-2) +'*')
    print('*' + ' '*(stars-2) +'*')
    print('*'* stars)


###################################################################
# Question 10
###################################################################
def draw_court():
    '''Overall setting'''
    s=turtle.Screen()
    t=turtle.Turtle(shape='turtle')
    t.speed(10)

    '''draw a rectangle with thick string'''
    t.width(5)
    t.penup()
    t.goto(-280,-150)
    t.pendown()
    t.color("black","yellow")
    t.begin_fill()
    t.forward(560)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(560)
    t.left(90)
    t.forward(300)
    t.end_fill()

    '''middle circle'''
    t.width(3)
    t.penup()
    t.goto(0,-150)
    t.pendown()
    t.setheading(90)
    t.forward(300)
    t.penup()
    t.goto(0,36)
    t.pendown()
    t.setheading(180)
    t.circle(36,360)

    '''three point line'''
    t.penup()
    t.goto(280,125)
    t.pendown()
    t.setheading(180)
    t.forward(31.4)
    t.circle(125,180)
    t.forward(31.4)

    '''three-second area'''
    t.penup()
    t.goto(280,60)
    t.pendown()
    t.color("black","orange")
    t.begin_fill()
    t.goto(164,36)
    t.goto(164,-36)
    t.goto(280,-60)
    t.goto(280,60)
    t.end_fill()

    '''free trow circle'''
    t.penup()
    t.goto(164,36)
    t.pendown()
    t.setheading(180)
    t.circle(36,360)
    t.penup()

    '''bracket and bound'''
    t.goto(248.6,4.5)
    t.pendown()
    t.circle(4.5,360)
    t.penup()
    t.goto(256,-18)
    t.pendown()
    t.goto(256,18)
    t.goto(256,0)
    t.goto(300,0)

    '''the other side'''
    t.penup()
    t.goto(-280,-125)
    t.pendown()
    t.setheading(0)
    t.forward(31.4)
    t.circle(125,180)
    t.forward(31.4)

    t.penup()
    t.goto(-280,60)
    t.pendown()
    t.color("black","orange")
    t.begin_fill()
    t.goto(-164,36)
    t.goto(-164,-36)
    t.goto(-280,-60)
    t.goto(-280,60)
    t.end_fill()

    t.penup()
    t.goto(-164,-36)
    t.pendown()
    t.setheading(0)
    t.circle(36,-360)
    t.penup()
    t.goto(-248.6,-4.5)
    t.pendown()
    t.circle(4.5,-360)
    t.penup()
    t.goto(-256,-18)
    t.pendown()
    t.goto(-256,18)
    t.goto(-256,0)
    t.goto(-300,0)

###################################################################
# Question 11
###################################################################
def projected_grade(a1,A1,a2,A2,m,M):
    '''(int) -> (int)
    calculate proportions of three assignments and mid-term and final-term exams
    and then sum up them by weight and we can get the Total grade'''
    P1 = a1/A1
    P2 = a2/A2
    P3 = (P1 + P2)/2
    P4 = m/M
    P5 = P4
    Total = (P1 + P2 + P3)*5 + P4*35 + P5*50
    return Total


###################################################################
# Question 12
###################################################################
def projected_grade_v2():
    '''(int) -> (int)
    guide the user to input grades perspectively and then use a branch to
    distinguish different algorithms.
    For people who doesn't reach 50 marks at the mid-term exam, use the mid-term
    exam grade as their final grade.
    For people who are higher than 50, use the algorithm of Question 11 to calculate
    their final grade''' 
    print("How many points did you get in Assignment 1?")
    a1 = int(input())
    print("What was the maximum possible number of points for Assignment 1?")
    A1 = int(input())
    print("How many points did you get in Assignment 2?")
    a2 = int(input())
    print("What was the maximum possible number of points for Assignment 2?")
    A2 = int(input())
    print("How many points did you get on the midterm?")
    m = int(input())
    print("What was the maximum possible number of points for the midterm?")
    M = int(input())

    if m/M > 0.5:
        print("Your predicted final grade is " + str(round(projected_grade(a1,A1,a2,A2,m,M),3)) + " %")
    else:
        print("Your predicted final grade is " + str(round(m/M*100,3)) + " %")
