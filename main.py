import time
from turtle import Screen
from paddle_pong import Paddle
from boal import Boal
from scoreboard import Scoreboard


#creare the screen
screen = Screen()
screen.setup(1376,768)
screen.bgcolor('black')

#create the boal
a_boal = Boal()

#crete the paddles
STARTING_POSITION_ONE = (-668, 0)
STARTING_POSITION_TWO = (668, 0)
paddle_one = Paddle(STARTING_POSITION_ONE)
paddle_two = Paddle(STARTING_POSITION_TWO)


#move paddle_ONE
screen.tracer(0)
screen.listen()
screen.onkey(paddle_one.paddle_up, 'w')
screen.onkey(paddle_one.paddle_down,'s')
#move paddle_TWO
screen.onkey(paddle_two.paddle_up, 'Up')
screen.onkey(paddle_two.paddle_down,'Down')

#scoreboard
PY1_SCORE_POSITION = (-100, 280)#sx
PY2_SCORE_POSITION = (100, 280)#dx

py1_scoreboard = Scoreboard(PY1_SCORE_POSITION)
py2_scoreboard = Scoreboard(PY2_SCORE_POSITION)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    a_boal.boal_move()

    if a_boal.ycor() >= 370 or a_boal.ycor() <= -360:
        a_boal.bounce()

    # detect collision with the paddle
    if a_boal.distance(paddle_one) < 60 and a_boal.xcor() < -648 or a_boal.distance(paddle_two) < 60 and a_boal.xcor() > 648:
        a_boal.bounce_paddle()


    #detect when the paddle misses boal

        #increase score
    if a_boal.xcor() > 668:
        py1_scoreboard.increase_score()
        a_boal.reset_speed()
        a_boal.invert_direction()
        a_boal.goto(0,0)
    elif a_boal.xcor() < -668:
        py2_scoreboard.increase_score()
        a_boal.reset_speed()
        a_boal.invert_direction()
        a_boal.goto(0, 0)



screen.exitonclick()