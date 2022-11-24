from turtle import Turtle

FONT = ('Arial', 24, 'normal')
ALIGNMENT = 'center'


def save_highest_score(score):
    with open("highest_score.txt", mode='w') as file:
        file.write(str(score))


def give_highest_score():
    with open("highest_score.txt", mode='r') as file:
        return int(file.read())

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = give_highest_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f'Score: {self.score} , highest score: {self.highest_score}', False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_screen()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            save_highest_score(self.highest_score)
        self.score = 0
        self.update_screen()
