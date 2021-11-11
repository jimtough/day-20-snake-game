from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def reset(self):
        for segment in self.segments:
            segment.goto(999, 999)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def change_heading(self, new_heading):
        self.head.setheading(new_heading)

    def up(self):
        if self.head.heading() != DOWN:
            self.change_heading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.change_heading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.change_heading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.change_heading(RIGHT)
