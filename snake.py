from turtle import Turtle


class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

    def create_snake(self):
        for p in range(3):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=-20 * p, y=0)
            self.body_segments.append(new_segment)

    def move_tail(self):
        for seg_index in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[seg_index - 1].xcor()
            new_y = self.body_segments[seg_index - 1].ycor()
            self.body_segments[seg_index].goto(new_x, new_y)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
