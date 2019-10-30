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


Let's get to the point
----------------------

A number which always stays the same isn't very helpful!  We need to make this number get bigger as the player goes past pipes. Let's add another variable to Barry to keep track of the score:

.. code:: python

    barry_the_bird.score = 0

You should add this just after you create Barry, the same place that we set him to be alive.

Now let's add some code to increment (add 1 to) the score when we go past a pipe.  Add this to the end of the update function:

.. code:: python

    if top_pipe.right < barry_the_bird.x:
            barry_the_bird.score += 1
            
But we still need to plug the score variable into the code that draws the number on the screen.

*Change the call to the* :code:`screen.draw.text` *function in your draw function so that is uses the score variable*

Why does the score go up so fast?!
----------------------------------
You've probably noticed now that when you fly through some pipes the score soars upwards for a short period, instead of just going up 1.  Can you think why this might be?

The reason is that the code we added is in the update function, which runs every frame.  The code we added will increment the score if the bird is past the pipe.  But the bird is past the pipe for the whole time it takes the pipe to get to the edge of the screen.  Every single frame while Barry is past the pipe the score goes up one.  This gives you an appreciation of how fast the computer is drawing frames!

The are several different ways to solve this problem.  If you have your own idea then go ahead and try it out - don't be afraid to ask a mentor if you want help.  Or, you can leave this for now and read on to see how we're going to solve it.

But first, a detour...

Being a lazy programmer
-----------------------
You might have noticed that there are some lines of code that we've had to type in twice in different places. Like :code:`barry_the_bird.alive = True`, we do it once in the game setup code, and then again in the :code:`reset()` function, which is called when Barry dies and the game starts again.  Well maybe it would make sense to just use the :code:`reset()` function at the beginning of the game as well!  Then we'd only need the code in one place.

Add a call to :code:`reset()` at the very end of the file.

Now we can delete the :code:`barry_the_bird.alive = True` call that happens in the game setup code.

*There is another line we can also now delete.  Go ahead and delete it*

We also want our score to go back to zero when the game resets. 

*Move the line that sets the score to zero up in to the reset function*

Check the everything still works the same as before.

End of detour: Let's fix the crazy score
----------------------------------------

Instead of adding 1 point each time we pass the pipes, let's number the pipes!  We'll assign a number to each pair of pipes and just set the score to be equal to that number when we go past.

At the beginning of the game the pipes on the screen are pair number 1.  Add this to the :code:`reset()` function:

.. code:: python

    top_pipe.pair_number = 1

We'll just keep track in the top pipe, don't worry about the bottom one.  

*Make it so that this number is incremented when we move the pipes back across to the right side of the screen*  

Hint : It happens in the update function

*Print out the new pair_number when you increment it and look at the log panel in Mu to verify it's working properly*

*Now modify the code where we change Barry's score.  Instead of incrementing it set it to be equal to the pair number.*

**Please ask a mentor for help if you're having trouble with any of these steps**

If you got to here and your score is now going up sensibly one at a time then well done indeed!!  This was a challenging section with a lot of work, so feel proud!

Explaining things to your future self
-------------------------------------
Our update function is getting pretty big now.  You might have found it's starting to take a while to read and figure out what does what. So it's about time we introduced **comments**. Comments are any text that you want to write in your file that you want the computer to ignore.  If you write helpful comments then it makes it easier for you, or even someone else to understand what your code is doing.  Let's add some comments so that our update function looks something like:

.. code:: python

  def update():
    # Barry's movement
    barry_the_bird.speed += gravity
    barry_the_bird.y += barry_the_bird.speed
    
    # Pipe movement
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    
    # Maybe move pipes to right side of screen
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH
        top_pipe.pair_number += 1
 
    # Check where barry is
    if barry_the_bird.y > HEIGHT or barry_the_bird.y < 0:
        # He went off the screen!
        reset()
        
    if (barry_the_bird.colliderect(bottom_pipe) or barry_the_bird.colliderect(top_pipe)):
        on_hit_pipe()
        
    # Maybe change the score
    if top_pipe.right < barry_the_bird.x:
        barry_the_bird.score = top_pipe.pair_number

Every line that starts with a # (it's called the hash symbol) is a comment and will be ignored by Python.  Normally a programmer would always be adding comments as they write code.  Feel free to add comments to your code as you work. Or to go back and add comments to code you already wrote.  It will make things easier for you!

Check the everything still works the same as before.



Something Random
----------------
To make the game more interesting we want the gap between the pipes to be at a different y position each time. To do this we need to generate a random number.

Often in Python you'll need to use the **import** keyword to get access to functions that aren't available by default.  These extra functions are grouped together in **modules**.  Let's import the :code:`random` module by adding these lines to the very top of your file:

.. code:: python

    import random
    print (random.randint(0,10))

The second line is to test the :code:`randint` function in the :code:`random` module.  If you run your game now you should see a number printed in the Mu log.  

*Start the game a few times to see what this function does.*

Hopefully you'll see that this function returns a random integer (whole number) in the range of the two arguments we gave it. So in this case, from 0 to 10.  Now that we've seen that we can remove the print line, but keep the import line.

Now let's use a random integer to move the gap up or down.  We'll do this in the update function, at the same time as when we move the pipes to the right side of the screen.  Our new helpful comments will make it easy to find the right place!  Find the lines which do :code:`right = WIDTH` for the pipes, and change them to:

.. code:: python

    offset = -150
    top_pipe.midleft = (WIDTH,offset)
    bottom_pipe.midleft = (WIDTH,offset + top_pipe.height + gap)

If you test it now you'll see that after the first set of pipes the gap is much higher (150 pixels higher to be precise).  Note that this doesn't affect the first set of pipes.

*Use the* :code:`random.randint` *function to move each pair of pipes to a random offset*

It's not Flappy Bird with out a flap
------------------------------------
So far our bird image is very static and the game should probably just be called "Bird".  Let's fix that now.

If you click on the **images** button in Mu you will see there are several bird images. So far we're using bird0 for the living bird, and birddead for the bird ghost.  We can also use bird1 or bird2 to liven things up a bit!

Add this code at the end of the update function:

.. code:: python

    # Animation
    if barry_the_bird.alive:
        if barry_the_bird.speed > 0:
            barry_the_bird.image = "bird1"
        else:
            barry_the_bird.image = "bird0"

Pay attention to the indentation here!  Any line that ends in a colon, like a function or an **if** statement has lines following that belong to it.  All the lines after it that have at least the next level of indentation belong to it.  So for the new :code:`if barry_the_bird.alive:` statement, all 4 lines after it are indented so they all belong to it.  They will only happen if Barry is alive!  (We need to make sure the bird image stays as a ghost when he's dead).  But, for the :code:`if barry_the_bird.speed > 0:` statement only the next line is indented, so only that one line depends on the :code:`if`.

The **else** keyword is new to us.  You can probably guess what it does.  An **if** can optionally have an **else** part after it.  The **else** part is what will happen if the value in the **if** statement is false. So our new code is using the "bird1" image when flying downwards (remember that we measure from the top of the screen, so a positive speed means going down), and using "bird0" when flying upwards.

**Ask a mentor now if this isn't working for you or you don't understand.**


