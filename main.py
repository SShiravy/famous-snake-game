# Create Snake body
# Move Snake
# Create snake food
# Detect collision with food
# Create a scoreboard
# Detect Collision with wall
# Detect Collision with tail
from gamePlay import start_game
from turtle import Screen

if __name__ == "__main__":
    # create the screen
    screen = Screen()
    screen.bgcolor('black')
    screen.title('famous snake game')
    screen.setup(width=600, height=600)
    screen.tracer(0)
    # ------
    start_game(screen)
    # ------
    screen.exitonclick()


