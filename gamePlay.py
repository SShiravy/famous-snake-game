
def start_game(snake_body_segments,screen):
    game_is_on = True
    while game_is_on:
        screen.update()
        for segment in snake_body_segments:
            segment.forward(20)
