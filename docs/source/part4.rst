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


