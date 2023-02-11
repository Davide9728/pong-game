#create de padlles pong
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, the_position):
        super().__init__()
        self.color('white')
        self.shape('square')

        self.penup()
        self.setpos(the_position)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def paddle_up(self): #paddle go up of 20 pixel
        new_y = self.ycor() + 20
        self.goto(self.xcor() ,new_y)


    def paddle_down(self): #paddle go down of 20 pixel
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
