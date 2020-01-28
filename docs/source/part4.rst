.. _part4:

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

Keeping Score!
--------------
* Add the following code to the end of your :code:`draw` function:

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

* Check that now when you play the game you see a number 7 at the top of the screen.

So why is this statement so big?  Well, it's because we're calling a function which takes a lot of **arguments**.  Arguments are like options.  When you call a function, if there are no arguments it looks like this:

.. code:: python

    make_toast()

This should look familiar to you, this is how we call our :code:`reset()` function, and our :code:`on_hit_pipe()` function.  But if you want to pass arguments then the function call looks like this:

.. code:: python

    make_sandwich(white_bread, cheese)  # Arguments are separated by a comma

The long statement we added above is a call to the :code:`screen.draw.text` function (It's a good name for a function that draws text on the screen!).  See how the function call has 4 arguments separated by commas.

*Can you figure out what each of these arguments does by changing them and testing the results?*

* Move the number so it's centered at the top of the screen 

Hint : Remember that :code:`WIDTH` contains the width of the screen

Normally programmers don't have to guess what arguments do.  It's much easier to read the instructions!  You can find the documentation of this function at:

https://pygame-zero.readthedocs.io/en/stable/ptext.html

* Add a drop shadow to the number

Hint: Look at the section titled "Drop Shadow" on that page.  You only need to add one more argument to the function call.  Ask a mentor for help if you have trouble getting this working.


Let's get to the point
----------------------

A number which always stays the same isn't very helpful!  We need to make this number get bigger as the player goes past pipes. Let's add another variable to Barry to keep track of the score.

.. Intentional mistake:

* Add this to the bottom of the file:

.. code:: python

    barry_the_bird.score = 0

Now let's add some code to increment (add 1 to) the score when we go past a pipe.  

* Add this to the end of the update function:

.. code:: python

    if top_pipe.right < barry_the_bird.x:
        barry_the_bird.score += 1
            
But we still need to plug the score variable into the code that draws the number on the screen.

* Change the call to the :code:`screen.draw.text` function in your draw function so that it uses the score variable

Why does the score go up so fast?!
----------------------------------
You've probably noticed now that when you fly through some pipes the score soars upwards for a short period, instead of just going up 1.  

*Can you think why this might be?*

The reason is that the code we added is in the update function, which runs every frame.  The code we added will increment the score if the bird is past the pipe.  But the bird is past the pipe for the whole time it takes the pipe to get to the edge of the screen.  Every single frame while Barry is past the pipe the score goes up one.  This gives you an appreciation of how fast the computer is drawing frames!

There are several different ways to solve this problem.  If you have your own idea then go ahead and try it out - don't be afraid to ask a mentor if you want help.  Or, you can leave this for now and read on to see how we're going to solve it.

Explaining things to your future self
-------------------------------------
Our update function is getting pretty big now.  It's starting to take a while to figure out what does what.   It's time to introduce **comments**! 

Comments are any text that you write in your file that you want the computer to ignore.  If you write helpful comments then it makes it easier for you, or even someone else to understand what your code is doing.  

Let's add some comments so that our update function looks something like this:

* Add the lines starting with #

.. code:: python

    def update():
        # Move Barry
        barry_the_bird.speed += gravity
        barry_the_bird.y += barry_the_bird.speed

        # Move pipes
        top_pipe.x += scroll_speed
        bottom_pipe.x += scroll_speed

        # Pipes off screen?
        if top_pipe.right < 0:
            top_pipe.left = WIDTH
            bottom_pipe.left = WIDTH

        # Barry off screen?
        if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
            reset()

        # Hit pipe?
        if (barry_the_bird.colliderect(top_pipe) or barry_the_bird.colliderect(bottom_pipe)):
            hit_pipe()

        # Change score?
        if top_pipe.right < barry_the_bird.x:
            barry_the_bird.score += 1

Every line that starts with # is a comment and will be ignored by Python.
  
Normally a programmer would always be adding comments as they write code.  Feel free to add comments to your code as you work. Or to go back and add comments to code you already wrote.  It will make things easier for you!

* Check the everything still works the same as before.


Let's fix the crazy score
-------------------------

Instead of adding 1 point each time we pass the pipes, let's number the pipes!  We'll assign a number to each pair of pipes and just set the score to be equal to that number when we go past.

At the beginning of the game the pipes on the screen are pair number 1.  

* Add this to the :code:`reset()` function:

.. code:: python

    top_pipe.pair_number = 1

We'll just keep track in the top pipe, we know the bottom one will always be part of the same pair.  

* Make it so that this number is incremented when we move the pipes back across to the right side of the screen

Hint : It happens in the update function.  Your new comments should help find the place.

* Print out the new :code:`pair_number` when you increment it and look at the log panel in Mu to verify it's working properly

* Modify the code where we change Barry's score.  Instead of incrementing it set it to be equal to the pair number.

**Please ask a mentor for help if you're having trouble with any of these steps**

If you got to here and your score is now going up sensibly one at a time then well done indeed!!  This was a challenging section with a lot of work, so feel proud!



Something Random
----------------
To make the game more interesting we want the gap between the pipes to be at a different **y** position each time. To do this we need to pick a random number.

Often in Python you'll need to use the **import** keyword to get access to functions that aren't available by default.  These extra functions are grouped together in **modules**.  

* Import the :code:`random` module by adding these lines to the very top of your file:

.. code:: python

    import random
    print (random.randint(1,6))

The second line is to test the :code:`randint` function in the :code:`random` module.  If you run your game now you should see a number printed in the Mu log.  

* Start the game a few times to see what this function does.

Hopefully you'll see that this function returns a random integer (whole number) in the range of the two arguments we gave it. So in this case, from 1 to 6.  Now that we've tried it we can delete the :code:`print` line, but keep the :code:`import` line.

Now let's use a random integer to move the gap up or down.  We'll do this in the update function, at the same time as when we move the pipes to the right side of the screen.  

* Find the 2 lines which do :code:`left = WIDTH` for the pipes, and change them to:

.. code:: python

    offset = -150
    top_pipe.midleft = (WIDTH,offset)
    bottom_pipe.midleft = (WIDTH,offset + top_pipe.height + gap)

If you test it now you'll see that after the first set of pipes the gap is much higher (150 pixels higher to be precise).  Note that this doesn't affect the first set of pipes.

* Use the :code:`random.randint` function to move each pair of pipes to a random offset

Hint: When testing changes like this you might want to make the :code:`gap` bigger so you don't have to spend so many attempts getting through the pipes.


It's not Flappy Bird with out a flap
------------------------------------
So far our bird image is very static and the game should probably just be called "Bird".  Let's fix that now.

If you click on the **images** button in Mu you will see there are several bird images. So far we're using "bird1" for the living bird, and "birddead" for the bird ghost.  We can also use "bird0" to liven things up a bit!

* Add this code at the end of the update function:

.. code:: python

    # Animation
    if barry_the_bird.alive:
        if barry_the_bird.speed > 0:
            barry_the_bird.image = "bird1"
        else:
            barry_the_bird.image = "bird0"

* Pay attention to the indentation here!  

Any line that ends in a colon, like a function or an **if** statement has lines following that belong to it.  All the lines after it that have at least the next level of indentation belong to it.  So for the new :code:`if barry_the_bird.alive:` statement, all 4 lines after it are indented so they all belong to it.  They will only happen if Barry is alive!  (We need to make sure the bird image stays as a ghost when he's dead).  But, for the :code:`if barry_the_bird.speed > 0:` statement only the next line is indented, so only that one line depends on the :code:`if`.

The **else** keyword is new to us.  You can probably guess what it does.  An **if** can optionally have an **else** part after it.  The **else** part is what will happen if the value in the **if** statement is false. So our new code is using the "bird1" image when flying downwards (remember that we measure from the top of the screen, so a positive speed means going down), and using "bird0" when flying upwards.

**Ask a mentor now if this isn't working for you or you don't understand.**



Bug Fix Challenges
------------------
Bugs are things that don't work quite right in your code.  Absolutely all code has bugs in it when it's first written.  Let's try to fix a couple now. For each bug you should follow this process:

1. Reproduce it.  This means checking that you can see the bug happen.
2. Figure out why it's happening.
3. Fix it!
4. Check that you can't reproduce it any more.

* **Bug #1**:  When you die and start again, your score at the top of the screen doesn't go back to zero.

* **Bug #2**:  If you crash in to the top pipe in just the right place your falling ghost can keep flying far enough to get a cheeky extra point.

Hint: You could try changing :code:`scroll_speed` to make it easier to reproduce this bug.

Well Done!!!
------------
You've written a complete fully working game! Take some time to enjoy playing your creation!  Remember there are values in the code like gravity, scroll_speed, and gap that you can tweak to try to make it more fun.

If you want to add more features to your game the PyZero documentation will help:

https://pygame-zero.readthedocs.io/en/stable/

If you want to add something to the game then talk to a mentor about how you might do it.  Here's a few things you might want to try:

- Make the bird stay still until the first flap

- A high score feature so you can see your best score.

- Starting the game with 3 lives so you can hit the pipes twice without dying

- Collectible stars

- Pipes that move up and down as they come towards you

- Variable scrolling speed.  Maybe flapping speeds you up





