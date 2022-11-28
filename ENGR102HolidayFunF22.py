'''This module contains several functions for drawing fun
holiday designs using turtle graphics. Start by calling the 
drawflake(), drawhand(), drawtree(), or drawsnowman()
functions, then have fun!

For more information on turtle graphics and a list of methods:
https://docs.python.org/3.3/library/turtle.html?highlight=turtle'''

import turtle as t
from math import sqrt

def drawtree():
    '''Draws a tree'''
    t.title("Happy Holidays!")
    t.up()
    t.left(90)
    t.forward(300)
    t.left(135)
    t.down()
    
    t.color('green')
    t.pensize(5)
    t.begin_fill()
    t.forward(100)
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(150)
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(175)
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(200)
    t.left(135)
    a = (100 + 150 + 175 + 200) * sqrt(2) / 2 - 150
    t.forward(a)
    
    t.up()
    t.left(90)
    t.forward(a+150)
    t.right(135)
    t.down()
    
    t.forward(100)
    t.right(135)
    t.forward(50)
    t.left(135)
    t.forward(150)
    t.right(135)
    t.forward(50)
    t.left(135)
    t.forward(175)
    t.right(135)
    t.forward(50)
    t.left(135)
    t.forward(200)
    t.right(135)
    t.forward(a)
    t.end_fill()
    t.up()
    
    t.down()
    t.color('rosy brown')
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.end_fill()
    t.up()
    t.right(180)

def drawstartop():
    '''Draws a yellow star with black outline'''
    b = 360 * 2 / 5
    t.color('black','yellow')
    t.begin_fill()
    t.forward(30)
    t.left(b / 2)
    t.forward(30)
    t.right(b)
    t.forward(30)
    t.left(b / 2)
    t.forward(30)
    t.right(b)
    t.forward(30)
    t.left(b / 2)
    t.forward(30)
    t.right(b)
    t.forward(30)
    t.left(b / 2)
    t.forward(30)
    t.right(b)
    t.forward(30)
    t.left(b / 2)
    t.forward(30)
    t.end_fill()

def drawornament(col = 'red'):
    '''Draws a round ornament using user defined color, default is red'''
    t.color(col)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def snowflake(n, k):
    '''Draws snowflake fractal, call drawflake() first'''
    #base case
    global counter
    if n <= 1:
        t.forward(k)
        return
    #recursive step
    snowflake(n - 1, k)
    t.left(60)
    snowflake(n - 1, k)
    t.right(120)
    snowflake(n - 1, k)
    t.left(60)
    snowflake(n - 1, k)
    counter += 1

def drawflake(a = 4):
    '''Set up snowflake fractal, a is the fractal iteration, try an integer between 1 and 7'''
    t.title("Happy Holidays!")
    t.speed(0)
    t.up()
    kval = [100, 75, 30, 10, 5, 2, 1]
    b = [50, 60, 80, 150, 200, 300, 500]
    if a > 7:
        k = 1
        t.back(500)
    else:
        k = kval[a - 1]
        t.back(b[a - 1])
    global counter
    counter = 0
    t.down()
    snowflake(a, k)
    t.right(120)
    snowflake(a, k)
    t.right(120)
    snowflake(a, k)

def drawhand(mycolor='saddle brown'):
    '''Draws a hand for a hand turkey, mycolor is the color'''
    t.title('Happy Thanksgiving!')
    t.up()
    t.goto(-50, -220)
    t.right(30)
    t.down()
    t.color(mycolor)
    t.begin_fill()
    t.circle(250, 60)
    t.left(50)
    t.forward(200)
    t.right(10)
    t.forward(250)
    t.circle(20, 172)
    t.forward(230)
    t.right(160)
    t.forward(250)
    t.circle(22, 172)
    t.forward(250)
    t.right(160)
    t.forward(270)
    t.circle(25, 173)
    t.forward(270)
    t.right(165)
    t.forward(250)
    t.circle(22, 172)
    t.forward(370)
    t.right(121)
    t.forward(200)
    t.circle(28, 168)
    t.forward(278)
    t.end_fill()
    t.hideturtle()

def beak():
    '''Draw a turkey beak'''
    t.begin_fill()
    t.forward(30)
    t.left(160)
    t.forward(30)
    t.right(160)
    t.forward(30)
    t.left(160)
    t.forward(30)
    t.left(90)
    t.forward(22)
    t.end_fill()

def leg():
    '''Turkey leg or snowman arm?'''
    t.forward(80)
    t.backward(20)
    t.right(30)
    t.forward(20)
    t.backward(20)
    t.left(60)
    t.forward(20)

def drawsnowman():
    '''Draws a snowman'''
    t.title("Let it snow, let it snow, let it snow!")
    t.up()
    t.right(90)
    t.forward(310)
    t.left(90)
    t.down()
    t.pensize(2)
    t.color('black', 'white')
    t.begin_fill()
    t.circle(150)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(250)
    t.right(90)
    t.down()
    t.begin_fill()
    t.circle(110)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(190)
    t.right(90)
    t.down()
    t.begin_fill()
    t.circle(75)
    t.end_fill()
    t.up()

drawtree()