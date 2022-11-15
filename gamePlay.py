from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

MOVE_DISTANCE = 20
SPEED = 0.1


def start_game(screen):
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    game_is_on = True
    while game_is_on:
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        sleep(SPEED)
        snake.move_tail()
        snake.head.forward(MOVE_DISTANCE)
        if snake.head.distance(food) < 20:
            food.new_food()
            scoreboard.increase_score()
            snake.grove_up()
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            game_is_on = False
        for segment in snake.body_segments[1:]:
            if snake.head.distance(segment) < 15:
                scoreboard.game_over()
                game_is_on = False
        screen.update()
