

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
        top_pipe.x += scroll_speed
        bottom_pipe.x += scroll_speed
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


Flying back to the start
------------------------
What happens when Barry falls off the bottom of the screen?  Right now you probably lose him forever.  Let's try to do something better.  Add this new function after the on_mouse_down function:

.. code:: python

    def reset():
        print ("Back to the start...")
        barry_the_bird.speed = 1
        barry_the_bird.center = (75, 350)
        top_pipe.center = (300, 0)
        bottom_pipe.center = (300, top_pipe.height + gap)
        
Each line in this function is assigning a value.  First it sets Barry's speed back to what it started as, then puts his center at an x,y position.  It also moves the pipes back to their starting points.  If you try the game now you'll see that nothing has changed.  Remember that a function won't do anything until you  **call** it.  Let's call it from the update function if Barry goes off the screen.  Add this to the end of the update function:  

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

This makes him move a whole 50 pixels all at once. Not very smooth!  When a real bird flaps its wings it changes the bird's speed, not its position. Change in position is just a side effect of having speed.  Let's try changing the :code:`on_mouse_down` function to this:

.. code:: python

    def on_mouse_down():
        barry_the_bird.speed = -6.5

Did that work?  Try it and you'll see that when you flap now he'll just go up and hit the top of the screen.  We need some gravity to pull him back down again after each flap!

Let's create a variable called gravity at the end of your file:

.. code:: python

    gravity = 0.3

And we'll use this to change the bird's speed every frame.  Add this to the beginning of the update function:

.. code:: python

  barry_the_bird.speed += gravity

*Try changing the value of gravity to see what effect it has*


Now this bird is more flappy!   Controlling him now takes a bit more skill.  You can try to fly through the gaps, but we still haven't done anything to stop you flying straight through the pipes.  We'll fix that soon. But first...

Being a lazy programmer
-----------------------
You might have noticed that there are some lines of code that we've had to type in twice in different places. For example, :code:`barry_the_bird.speed = 1`. We do it once in the game setup code, and then again in the :code:`reset()` function, which is called when Barry dies and the game starts again.  Well maybe it would make sense to just use the :code:`reset()` function at the beginning of the game as well!  Then we'd only need the code in one place.

Add a call to :code:`reset()` at the very end of the file.

Now we can delete the :code:`barry_the_bird.speed = 1` call that happens in the game setup code.

*Can you figure out a way  to specify the position of everthing in just one part of the code?*   

Hint:  You should be able to remove 3 position values.  One of them looks like:  :code:`(75, 350)`

Check the everything still works the same as before.

Giving Barry a head start
-------------------------
Let's give the player a bit more time to flap before they fall off the screen.  We can move the start point to just 50 pixels away from the top of the screen.  Find this line in the reset function:

.. code:: python

    barry_the_bird.center = (75, 350)

And change the 350 to something much smaller.  Maybe 50?  Try it and find a value that seems right to you.

Isn't it great this number is only in one place in the code?   If we hadn't done the last section (Being a lazy programmer) we would have to change two different numbers!  It would have been very easy to forget about one of them.


Collisions
----------
In PyGameZero there's nothing to stop you drawing multiple sprites (images) on top of each other.  So if we want certain behaviour when things collide we need to take care of it ourselves.  Add this code to the end of the update function:

.. code:: python

    if (barry_the_bird.colliderect(top_pipe)):
        hit_pipe()

The :code:`colliderect` function checks if two objects are touching.  Because this is inside the update function it will get checked every frame.  This won't work yet because we haven't created the :code:`hit_pipe` function.  Let's create it after the :code:`reset` function...

.. code:: python

    def hit_pipe():
        print ("Hit pipe!")
        barry_the_bird.image = "birddead"

Try this out.  Now Barry should become a ghost when you hit the bottom pipe, but it looks like there are still three problems:

 1. Barry stays as a ghost even when the game resets.
 2. Barry can still fly through the bottom pipe!
 3. You can still flap and fly along even as a ghost.

*Try to fix problems 1 & 2 now.*   Once you've done that we'll look at fixing number 3 together.  Here are some hints if you need them:

Hint for number 1 : Barry started with the "bird1" image, but it changes to "birddead" when he hits a pipe.  Find the right place to change it back.

Hint for number 2 : Remember the :code:`or` keyword.


Now might be a good time to try changing the size of :code:`gap` to tune the difficulty of the game.  You might want to make it very big while testing, so you can focus on testing and not on flying!

Now we'd like to stop Barry from flapping while he's a ghost.  The code which makes him fly needs a way of knowing if he's still alive. We could use the :code:`barry_the_bird.image` variable, because that changes when he dies.  But it's better to add a new variable to make our code cleaner and less likely to break if we make changes later.

Add this line to the :code:`reset` function (Being a lazy programmer pays off again!):

.. code:: python

    barry_the_bird.alive = True

We're creating the new variable :code:`alive` and setting it to true.  Now we need to make sure barry only flaps when he's alive.  Add this line to the beginning of the on_mouse_down function:

.. code:: 

    if (barry_the_bird.alive):

Don't forget to change the indentation (number of spaces at the beginning) of the line that changes the speed, so that it's part of the **if** statement.  We only want to change the speed (in other words flap) **if** the bird is alive!

The next thing to do is to change barry to not be alive when he hits a pipe.

*Challenge : Add a line to change barry's* :code:`alive` *variable to* :code:`False` *when he hits a pipe.*



Well done.  That's the end of part 3.   In the next part we'll look at a few finishing touches such as adding a flapping animation, randomizing the pipe positions, and keeping score.
    
Extra Challenges
----------------

* *Turn physics upside down!  Make gravity pull Barry upwards, and make flapping push him downwards*

* *Add a cheat key that makes the player invincible*  
 
Hint: Try adding this function and see what happens when you press a key:

.. code:: python

    def on_key_down(key):
        print(key)

* *Add a secret tiny flap that the player can do using the right mouse button*

Hint: you will need to add a **parameter** to your :code:`on_mouse_down` function, so it becomes :code:`on_mouse_down(button)`.  Try use the :code:`print` function like you did in the last challenge to see what values :code:`button` has.



