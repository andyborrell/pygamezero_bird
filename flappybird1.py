TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

def update():
    barry_the_bird.y += barry_the_bird.speed

def draw():
    screen.blit('background', (0, 0))
    barry_the_bird.draw()

def on_mouse_down():
    print ('The mouse was clicked')
    barry_the_bird.y -= 50

barry_the_bird = Actor('bird1', (75, 350))
barry_the_bird.speed = 1