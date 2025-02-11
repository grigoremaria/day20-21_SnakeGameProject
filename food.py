import random
from turtle import Turtle

#TODO 4: detect collision with food - when the snake gets the food, square +1 and
#       a new piece of food is created randomly on the screen at some sort of random location

score = 0

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        #we are able to use shape, penup etc because we inheritace from the Turtle class

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        #score += 1
        # food is created randomly on the screen