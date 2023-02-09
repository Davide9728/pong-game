#create the boal and make it move
from turtle import Turtle

class Boal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.move_x = 10
        self.move_y = 10




    def boal_move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1.5

    def invert_direction(self):
        self.move_x *= -1

    def reset_speed(self):
        self.move_x = 10
        self.move_y = 10

