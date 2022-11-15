from turtle import Turtle

FONT = ('Arial', 24, 'normal')
ALIGNMENT = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f'Score: {self.score}', False, ALIGNMENT,FONT)

    def increase_score(self):
        self.score += 1
        self.update_screen()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',False,ALIGNMENT,FONT)
