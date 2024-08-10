from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 2
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(10)
        self.go_to_start()
        self.setheading(90)
        self.move_distance = MOVE_DISTANCE  # Initialize move distance

    def go_up(self):
        self.forward(self.move_distance)
        self.move_distance += MOVE_INCREMENT  # Increase speed after each move

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.move_distance = MOVE_DISTANCE  # Reset move distance after each level

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
