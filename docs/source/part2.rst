.. _part2:

Part 2
======

So now you have a background and a bird that flys up and down, let's add the pipes that the bird must fly through.


Adding the pipes
----------------

You've already seen that we can create :code:`Actor` objects and move these around the screen. If you've forgotten, go and look at where you use :code:`barry_the_bird` in your code to see how it works.

So we need to add two pipes, and if you look in the :code:`images` directory you'll see we have two files named :code:`top.png` and :code:`bottom.png`. How do we add these to the game?

Let's create two new actors, at the end of your code add:

.. code:: python

   top_pipe = Actor('top', (300,0))
   bottom_pipe = Actor('bottom', (300,500))

We mustn't forget to draw these pipes, so add this to your :code:`draw` function:

.. code:: python

   top_pipe.draw()
   bottom_pipe.draw()

- Press **play** to see the effect.

Great we have some pipes! But they are just sitting there on the page and there's no gap between them.


Mind the gap
------------

How do we make a gap for our bird to fly through? We need to make sure we position the pipes in the right place on the screen, and to do this we need to know how big each image is.

Let's see what we can find out from an actor, add this code at the end of your program:

.. code:: python

   print(top_pipe.height, top_pipe.width)

- Press **play** and look in the bottom half of your code window. 

You should see two numbers appear (I get :code:`500 100`), that's the width and height of the top pipe.

Using that info, we can change the definition of the top and bottom pipes to this:

.. code:: python

   gap = 100
   top_pipe = Actor('top', (300, 0))
   bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))

Hang on a minute, where did that maths come from? Well :code:`gap` is just a variable and we add it on to the height of the top pipe. Try changing the value and see what happens.


You know when to press play
---------------------------

You've been pressing play a lot haven't you? That's how you see the effect of your code changes.

From now on we're going to stop telling you when to press play and just encourage you to try running your code when you've completed each litte code box, or when you feel like it.

Sometimes you'll see an error, in which case: read the last line of the error, think about what you just changed and get investigating. You can always ask a mentor if you are really stuck.


Flying forwards
---------------

So now that we have the pipes, let's get them moving.

  Note: Smoke and Mirrors

  You might be thinking "doesn't the player fly forward and the pipes stay still?"

  If you thought that, then the game fooled you. It's a good trick. It looks like the player is moving forward. But in reality, the player stays still and everything else moves backwards.

So let's make the pipes move. Just as we did with our bird we can add a speed variable to the pipes and use this to move them. We want these first two lines of code to run once when we run the program, so they need to go at the end of your code:

.. code:: python

   top_pipe.speed = 1
   bottom_pipe.speed = 1

And this code needs to run repeatedly, so it goes in the :code:`update` function:

.. code:: python

   top_pipe.x += top_pipe.speed
   bottom_pipe.x += bottom_pipe.speed

Oh no! Why are the pipes moving the wrong way? Can you fix it? Hint: when setting the speed, what's the opposite of 1? 


More pipes
----------

We need more pipes, one set is not enough. But actually we have enough already, we can just loop them round when they go off the screen.

To do this, let's meet the very handy :code:`if` statement and two of its friends, greater-than :code:`>` and less-than :code:`<`...

What do you think this code does? Open a new Mu script and type it in:

.. code:: python
          
   a = 10
   if a > 5:
     print("Wow a is big")

- To run this you'll need to save it first, just pick a filename such as :code:`test.py`.

What about this:

.. code:: python
          
   a = 10
   if a < 5:
     print("Wow a is small")

So as you can see (hopefully!) :code:`if` tests somethnig, in the first example if the variable :code:`a` is greater than 5, and then does whatever you tell it to do.

There are two tricky things to get right with :code:`if` statements:

* Exactly what are you testing? What goes after the :code:`if`?
* Get your indentation right -- how many spaces at the start of the line -- so that the right code is run.


Looping the pipes
-----------------

OK, let's get to work in the :code:`update` function, as that's where we move them. Add this code to the end of the function, and make sure you indent it so that it really is inside the function -- this is hard to explain, ask a mentor for help. 

.. code:: python

   if top_pipe.x < 0:
     top_pipe.x = WIDTH

OK, that's not bad, but two problems...

1. Only the top pipe moves
1. The pipe dissappears too quickly, before it's left the side of the screen

Can you fix these issues?


Ouch!
-----

OK, it's time to deal with collisions, this is going to be painful, but don't worry, no actual birds are going to be harmed -- only virtual birds.

To be continued...

