from turtle import Turtle

#create the boal and make it move
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.move_x = 10
        self.move_y = 10




    def boal_move(self): # it make ball moving, increasing coordinates of position
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self): # it change ball's direction when collide with a wall
        self.move_y *= -1

    def bounce_paddle(self): # it change ball's direction when collide with paddle
        self.move_x *= -1.5

    def invert_direction(self): # used when ball have to restart from middle after a point, it will chage initial direction of ball
        self.move_x *= -1

    def reset_speed(self): # reset default speed, used when ball come back to starting position
        self.move_x = 10
        self.move_y = 10

