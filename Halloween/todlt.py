# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 05:04:09 2020

@author: 19240179
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:22:25 2020

reference: https://towardsdatascience.com/simple-fun-python-project-for-halloween-ff93bbd072ad

You give the user a chance to pick an option — Trick or Treat. If the choice is to treat, then you just show a single turtle hit the finish line, and you are awarded a cookie for winning. The image, as well as the voice recording, needs to suggest the reward for the victory. If the choice selected is a trick, then the user gets to place a bet on the two turtles available. So the user has a 50% chance to win a reward of a cake else he gets no reward.
An Additional else case of rock, paper, scissor game can also be added to provide the user with a higher chance to win the game if they lose the first 50% chance.

@author: SA1987
"""

import turtle 
from turtle import *
from random import randint
from gtts import gTTS
from playsound import playsound
from PIL import Image

def treat():
    speed(0)
    penup()
    goto(-140, 140)
    for step in range(15):
        write(step, align='center')
        right(90)
        for num in range(8):
            penup()
            forward(10)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)
    
    turtle1 = Turtle()
    turtle1.color('blue')
    turtle1.shape('turtle')
    
    turtle1.penup()
    turtle1.goto(-160, 50)
    turtle1.pendown()
    
    for i in range(100):
        x = randint(1,5)
        turtle1.forward(x)
        
    turtle.exitonclick()
    
    tts = gTTS("Congratulations On Your Cookies!")
    tts.save("1.mp3")
    playsound("1.mp3")
    
    img = Image.open("cookie.jpg")
    img.show()
    
    
def trick(pick="red"):
    speed(0)
    penup()
    goto(-140, 140)

    for step in range(15):
        write(step, align='center')
        right(90)
        for num in range(8):
            penup()
            forward(10)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)
    
    turtle1 = Turtle()
    turtle1.color('red')
    turtle1.shape('turtle')

    turtle1.penup()
    turtle1.goto(-160, 100)
    turtle1.pendown()

    for turn in range(10):
        turtle1.right(36)

    turtle2 = Turtle()
    turtle2.color('blue')
    turtle2.shape('turtle')


    turtle2.penup()
    turtle2.goto(-160, 40)
    turtle2.pendown()
    
    total_x = 0
    total_y = 0

    for turn in range(100):

        x = randint(1,5)
        y = randint(1,5)

        total_x += x
        total_y += y

        turtle1.forward(x)
        turtle2.forward(y)

    turtle.exitonclick()
    print(total_x, total_y)
    
    if pick == "red" and total_x > total_y:
            tts = gTTS("Your Turtle Won! Congratulations On Your Cake!")
            tts.save("3.mp3")
            playsound("3.mp3")

            img = Image.open("Cake.jpg")
            img.show()
            
    elif pick == "blue" and total_y>total_x:
        
            tts = gTTS("Your Turtle Won! Congratulations On Your Cake!")
            tts.save("4.mp3")
            playsound("4.mp3")

            img = Image.open("cake.jpg")
            img.show() 
        
    else:
            pass 
    
print(''' Make Your Numerical Choice: 
1. Trick
2. Treat
''')
#choice = int(input(" "))

choice = 1
if choice == 1:
    str1 = input("Enter red or blue: ")
    #str1 = "red"
    trick(str1)

if choice == 2: 
    treat()