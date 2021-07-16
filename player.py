from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def start_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        turtle_up = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), turtle_up)

    def go_down(self):
        turtle_down = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), turtle_down)
