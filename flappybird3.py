TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

def update():
    barry_the_bird.speed += gravity
    barry_the_bird.y += barry_the_bird.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH
    if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
        reset()
    if (barry_the_bird.colliderect(top_pipe) or barry_the_bird.colliderect(bottom_pipe)):
        hit_pipe()

def draw():
    screen.blit('background', (0, 0))
    barry_the_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()

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
reset()