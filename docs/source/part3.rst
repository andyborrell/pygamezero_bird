

Part 3
======

Starting point
--------------
At this point your code should look like this:

.. code:: python

    TITLE = 'Flappy Bird'
    WIDTH = 400
    HEIGHT = 708

    def update():
        barry_the_bird.y += barry_the_bird.speed
        top_pipe.x += top_pipe.speed
        bottom_pipe.x += bottom_pipe.speed
        if top_pipe.right < 0:
            top_pipe.left = WIDTH
            bottom_pipe.left = WIDTH

    def draw():
        screen.blit('background', (0, 0))
        barry_the_bird.draw()
        top_pipe.draw()
        bottom_pipe.draw()

    def on_mouse_down():
        print ('The mouse was clicked')
        barry_the_bird.y -= 50

    barry_the_bird = Actor('bird1', (75, 350))
    barry_the_bird.speed = 1

    gap = 140
    top_pipe = Actor('top', (300, 0))
    bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))
    scroll_speed = -1
    top_pipe.speed = scroll_speed
    bottom_pipe.speed = scroll_speed


Flying back to the start
------------------------
What happens when Barry falls off the bottom of the screen?  Right now you probably lose him forever.  Let's try to do something better.  Add this new function after the on_mouse_down function:

.. code:: python

    def reset():
        print ("Back to the start...")
        barry_the_bird.speed = 0
        barry_the_bird.center = (75, 100)
        top_pipe.center = (300, 0)
        bottom_pipe.center = (300, top_pipe.height + gap)
        
Each line in this function is assigning a value.  First it sets barry's speed back to zero, then puts his center at an x,y position.  It also moves the pipes back to their starting points.  If you try the game now you'll see that nothing has changed.  Remember that a function won't do anything until you  **call** it.  Let's call it from the update function if barry goes off the screen.  Add this to the end of the update function:  

.. code:: python

    if barry_the_bird.y > HEIGHT:
        reset()

Make sure you indent it so that it's part of the update function, but not part of the previous **if** statement.  Indenting means adding the right number of spaces to the beginning of the line.  Now check that everthing resets if Barry falls off the bottom of the screen.  Ask a mentor for help if you have trouble getting this to work.

We also need to reset the game if Barry goes off the top of the screen.

*Can you make that happen?* 
Hint: you will need the :code:`or` keyword.


Time to Flap!
-------------
At the moment, Barry the bird seems to teleport upwards when you click the screen (play the game now if you don't remember).  We'd really like him to move a bit more smoothly.  The reason he seems to move instantaneosly is this line:

.. code:: python

    barry_the_bird.y -= 50

This makes him move a whole 50 pixels all at once. Not very smooth!  When a real bird flaps its wings it changes the bird's speed, not its position. Change in position is just a side effect of having speed.  Let's try changing the on_mouse_down function to this:

.. code:: python

    def on_mouse_down():
        barry_the_bird.speed -= 6.5

Did that work?  Try it and you'll see that when you flap now he'll just go up and hit the top of the screen.   We need some gravity to pull him back down again after each flap!

Let's create a variable called gravity at the end of your file:

.. code:: python

    gravity = 0.3

And we'll use this to change the bird's speed every frame.  Add this to the beginning of the update function:

.. code:: python

  barry_the_bird.speed += gravity

*Try changing the value of gravity to see what effect it has*


Now this bird is more flappy!   Controlling him now takes a bit more skill.  You can try to fly through the gaps, but we still haven't done anything to stop you flying straight through the pipes.  Let's fix that next...



