from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
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

def is_character_meet_hand():
    global x, y, hand_point, character_meet_hand
    if (round(x) == hand_point[0] and round(y) == hand_point[1]):
        character_meet_hand = True


def character_move_to_hand(hand_point):
    global x, y, speed, flip
    move_speed = speed / 100
    if hand_point[0] - x < 0: flip = 'h' 
    else: flip = 'n'
    x = (1 - move_speed) * x + move_speed * hand_point[0]
    y = (1 - move_speed) * y + move_speed * hand_point[1]


character_meet_hand = True
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
speed = 3
hide_cursor()
hand_point = (0, 0)
flip = 'n'

while running:
    clear_canvas()

    if character_meet_hand:
        hand_point = create_hand_random_point()
    character_move_to_hand(hand_point)
    is_character_meet_hand()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(*hand_point)
    character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, flip, x, y, 100, 100)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

    delay(0.01)

close_canvas()