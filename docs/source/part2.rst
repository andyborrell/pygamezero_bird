.. _part2:

Part 2
======

So now you have a background and a bird that flys up and down, let's add the pipes that the bird must fly through.


Adding the pipes
----------------

You've already seen that we can create :code:`Actor` objects and move these around the screen. If you've forgotten, go and look at where you use :code:`barry_the_bird` in your code to see how actors works.

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

You should see two numbers appear (I get 500 100), that's the width and height of the top pipe.

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

Sometimes you'll an error, in which case, read the last line, think about what you just changed and get investigating. You can always ask a mentor if you are really stuck.


Flying forwards
---------------

...
