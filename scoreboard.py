#keep score
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.score = 0
        self.print_score()


    def print_score(self):
        self.write(f"{self.score}", False,'center',('arial',76,'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, 'center', ('arial', 76, 'normal'))


    def end_tite(self):
        pass