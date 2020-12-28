import random

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

def update():
    # Move Barry
    barry_the_bird.speed += gravity
    barry_the_bird.y += barry_the_bird.speed

    # Move pipes
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

    # Pipes off screen?
    if top_pipe.right < 0:
        offset = random.randint(-175, 175)
        top_pipe.midleft = (WIDTH,offset)
        bottom_pipe.midleft = (WIDTH,offset + top_pipe.height + gap)
        top_pipe.pair_number += 1

    # Barry off screen?
    if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
        reset()

    # Hit pipe?
    if (barry_the_bird.colliderect(top_pipe) or barry_the_bird.colliderect(bottom_pipe)):
        hit_pipe()

    # Change score?
    if top_pipe.right < barry_the_bird.x:
        barry_the_bird.score = top_pipe.pair_number

    # Animation
    if barry_the_bird.alive:
        if barry_the_bird.speed > 0:
            barry_the_bird.image = "bird1"
        else:
            barry_the_bird.image = "bird0"

def draw():
    screen.blit('background', (0, 0))
    barry_the_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()

    screen.draw.text(
    str(barry_the_bird.score),
    color='white',
    midtop =(20, 10),
    fontsize=70,
    shadow=(1, 1)
    )

def on_mouse_down():
    if (barry_the_bird.alive):
        barry_the_bird.speed = -6.5

def reset():
    print ("Back to the start...")
    barry_the_bird.speed = 1
    barry_the_bird.center = (75, 100)
    barry_the_bird.image = "bird1"
    barry_the_bird.alive = True
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    top_pipe.pair_number = 1
    barry_the_bird.score = 0

def hit_pipe():
    print ("Hit pipe!")
    barry_the_bird.image = "birddead"
    barry_the_bird.alive = False

barry_the_bird = Actor('bird1')
gap = 140
top_pipe = Actor('top')
bottom_pipe = Actor('bottom')
scroll_speed = -1
gravity = 0.3
barry_the_bird.score = 0
reset()