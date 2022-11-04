from turtle import Turtle


def snake_body():
    snake_body_segments = []
    for p in range(2):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(x=-20 * p, y=0)
        snake_body_segments.append(new_segment)
    return snake_body_segments

