from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Python Pong Game")
screen.tracer(0)

r_paddle = Paddle(350,0)

l_paddle = Paddle(-350,0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(screen.bye, "q")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


# game_is_on = True
# while game_is_on:
#     screen.update()
#     ball.move()
def game_loop():
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        ball.move_speed = ball.move_speed*0.9
        # print(ball.move_speed)
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

   

    # if ball.xcor()>380:
    #     ball.direction_x=-1
    # if ball.xcor()<-380:
    #     ball.direction_x=1
    screen.ontimer(game_loop,int(ball.move_speed))

game_loop()
# screen.mainloop()

screen.exitonclick()