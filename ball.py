from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction_x=1
        self.direction_y=1
        self.move_speed = 100

    def move(self):
        new_x = self.xcor()+10*self.direction_x
        new_y = self.ycor()+10*self.direction_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.direction_y *= -1

    def bounce_x(self):
        self.direction_x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()