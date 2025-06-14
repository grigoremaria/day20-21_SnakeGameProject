
from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)] #create tuples
# in py constants are named in all caps
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() #create method
        self.head = self.segments[0]

    # TODO 1: create a snake body - 3 squares on the screen all lined up next to each other

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())


    # TODO 2: move the snake - continously move forward and change direction

    def move(self):
     #for seg_num in range(start= 2, stop= 0, step= -1) range is from C# and does not support arguments like start etc
        for seg_num in range(len(self.segments) - 1, 0, -1 ):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    #TODO 3: control the snake - using keyboard controls (up, left, down, right arrow keys)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
