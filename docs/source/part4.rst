Part 4
======

Starting point
--------------
At this point your code should look like this:

.. code:: python
    
    TITLE = 'Flappy Bird'
    WIDTH = 400
    HEIGHT = 708
    
    def update():
        barry_the_bird.speed += gravity
        barry_the_bird.y += barry_the_bird.speed
        top_pipe.x += top_pipe.speed
        bottom_pipe.x += bottom_pipe.speed
        if top_pipe.right < 0:
            top_pipe.left = WIDTH
            bottom_pipe.left = WIDTH
        if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
            reset()
        if (barry_the_bird.colliderect(bottom_pipe) or barry_the_bird.colliderect(top_pipe)):
            on_hit_pipe()
    
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
        barry_the_bird.image = "bird0"
        barry_the_bird.alive = True
        top_pipe.center = (300, 0)
        bottom_pipe.center = (300, top_pipe.height + gap)
        
    def on_hit_pipe():
        print ("Hit pipe!")
        barry_the_bird.image = "birddead"
        barry_the_bird.alive = False
        
    barry_the_bird = Actor('bird1', (75, 350))
    barry_the_bird.speed = 1
    barry_the_bird.alive = True
    
    gap = 140
    top_pipe = Actor('top', (300, 0))
    bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))
    scroll_speed = -1
    top_pipe.speed = scroll_speed
    bottom_pipe.speed = scroll_speed
    gravity = 0.3   

Keeping Score!
--------------
Add the following code to the end of your :code:`draw` function:

.. code:: python

    screen.draw.text(
            str(7),
            color='white',
            midtop =(20, 10),
            fontsize=70,
        )

This looks like a lot of code, but this is actually just one command (called a **statement** in programming languages).  Up until now every **statement** we've used took up just one line, but this line is different.  Python knows that the statement doesn't end on the first line, because the "(" doesn't have matching ")" on that line, so it takes all the following lines up to the matching ")" as part of the same statement.  That means that the following code wouldn't work:

.. code:: python

    # BAD CODE.  Don't type this in!
    # Python will think this next line is a whole statement and will get confused:
    screen.draw.text
        (
            str(7),
            color='white',
            midtop =(20, 10),
            fontsize=70,
        )

Python would think that :code:`screen.draw.text` is a whole statement, and that doesn't make sense to it.

Hopefully now when you play the game you see a number 7 at the top of the screen.

So why is this statement so big?  Well, it's because we're calling a function which takes a lot of **arguments**.  Arguments are like options.  When you call a function, if there are no arguments it looks like this:

.. code:: python

    make_toast()

This should look familiar to you, this is how we call our :code:`reset()` function, and our :code:`on_hit_pipe()` function.  But if you want to pass arguments then the function call looks like this:

.. code:: python

    make_sandwich(white_bread, cheese)  # Arguments are separated by a comma

The long statement we added above is a call to the screen.draw.text function (It's a good name for a function that draws text on the screen!).  See how the function call has 4 arguments separated by commas.

*Figure out what each of these arguments does by changing them and testing the results*

*Move the number so it's centered at the top of the screen* Hint : Remember that :code:`WIDTH` contains the width of the screen

Normally programmers don't have to guess what arguments do.  It's much easier to read the instructions!  You can find the documentation of this function at:

https://pygame-zero.readthedocs.io/en/stable/ptext.html

*Add a drop shadow to the number*  

Hint: Look at the section titled "Drop Shadow" on that page.  You only need to add one more argument to the function call.  Ask a mentor for help if you have trouble getting this working.


