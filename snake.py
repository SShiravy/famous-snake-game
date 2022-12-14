from turtle import Turtle


class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

    def create_snake(self):
        for p in range(3):
            self.add_segment((-20 * p,0))

    def move_tail(self):
        for seg_index in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[seg_index - 1].xcor()
            new_y = self.body_segments[seg_index - 1].ycor()
            self.body_segments[seg_index].goto(new_x, new_y)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.body_segments.append(new_segment)

    def grove_up(self):
        self.add_segment(self.body_segments[-1].position())

    def up(self):
        if self.head.heading() != 270:  # DOWN
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # UP
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:  # Right
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:  # left
            self.head.setheading(0)

    def reset(self):
        for segment in self.body_segments:
            segment.goto(1000,1000)
        self.body_segments.clear()
        self.create_snake()
        self.head = self.body_segments[0]
