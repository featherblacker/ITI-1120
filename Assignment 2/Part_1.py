# Student name: Qiguang Chu
# Student number: # 300042722
# Course: ITI 1120
# Assignment #2   part 1

import random

def questions(b,a):
    
    '''(int(),int() -> int())
    this function contract two integers to know the type and number of questions, which
    called by perform test and then produce questions and check if the answer people
    reply is true If it is not true, the function will print the right answer.'''

    m = 0
    i = 0
    if b == 0:
        while i < a:
            c = random.randint(1,9)
            d = random.randint(1,9)
            print(c, " + ", d, " = ", end = "")
            e = int(input())
            if e == (c+d):
                m = m + 1
            else:
                print("Incorrect - the answer is", c+d)
            i = i + 1
        return m
            
    if b == 1:
        while i < a:
            c = random.randint(1,9)
            d = random.randint(1,9)
            print(c, " * ", d, " = ", end = "")
            e = int(input())
            if e == (c*d):
                m = m + 1
            else:
                print("Incorrect - the answer is", c*d)
            i = i + 1
        return m


def perform_test(b,a):
    '''(int(),int()) -> String()
    this function is called by main function, which abstract two integers
    and then delivery it question(), after the calculation, the function gets
    the number of right answers and print the final evaluation.'''
    m = questions(b,a)
    if m/a >= 0.8:
        print("Well done! Congratulations.")
    else:
        if m/a >= 0.6:
            print("Not too bad but please study and practice some more.")
        else:
                print("Please study more and ask your teacher for help.")


'''This is used to print the first few lines to guide people who attends this test
Let him to input the type and number of questions and then use perform_test funtion to call question warehouse'''

print("Welcome to addition / multiplication test\n")
print("How many questions would you like to be tested on?")
print("Enter a non negative integer for the answer: ", end = "")
a = int(input())
print("This software tests you with ",a," questions …… ")
print("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1):",end = "")
b = int(input())
print("Please give the answers to the following multiplications:")
perform_test(b,a)



