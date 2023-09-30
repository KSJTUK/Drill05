from pico2d import *
import random

# test
TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def create_hand_random_point():
    global character_meet_hand
    rand_point = (random.randint(30, TUK_WIDTH - 30), random.randint(30, TUK_HEIGHT - 30))
    character_meet_hand = False
    return rand_point

def character_move_to_hand(hand_point):
    pass

character_meet_hand = True
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
hand_point = (0, 0)

while running:
    clear_canvas()

    if character_meet_hand:
        hand_point = create_hand_random_point()
    character_move_to_hand(hand_point)

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(*hand_point)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




