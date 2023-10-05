from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0,7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x , self.y =random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y > 40:
            self.y -= random.randint(0,10)
        else:
            self.y = 40
    def draw(self):
        self.image.draw(self.x,self.y)
class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 40:
            self.y -= random.randint(0, 10)
        else:
            self.y = 40

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global balls
    global world
    global big_balls
    running = True
    world = []

    grass = Grass()
    world.append(grass)

    balls = [Ball() for i in range(10)]
    big_balls = [Big_ball() for i in range(10)]

    world += balls
    world += big_balls

def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
