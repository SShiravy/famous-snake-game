from time import sleep
from snake import Snake

MOVE_DISTANCE = 20
SPEED = 0.25


def start_game(screen):
    snake = Snake()
    game_is_on = True
    while game_is_on:
        screen.listen()
        screen.onkey(snake.up,"Up")
        screen.onkey(snake.down,"Down")
        screen.onkey(snake.left,"Left")
        screen.onkey(snake.right,"Right")
        sleep(SPEED)
        snake.move_tail()
        snake.head.forward(MOVE_DISTANCE)
        screen.update()

