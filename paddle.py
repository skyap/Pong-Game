from turtle import Turtle

UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.create_paddle()


    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(self.x_pos,self.y_pos)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
