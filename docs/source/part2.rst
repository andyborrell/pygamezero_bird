.. _part2:

Part 2
======

So now you have a background and a bird that flys up and down, let's add the pipes that the bird must fly through.


Adding the pipes
----------------

You've already seen that we can create :code:`Actor` objects and move these around the screen. If you've forgotten, go and look at :code:`barry_the_bird` to see how it works.

So we need to add two pipes, and if you look in the :code:`images` directory you'll see we have two files named :code:`top` and :code:`bottom`. How do we add these to the game?

Let's add two new actors, at the end of your code add:

.. code:: python

   top_pipe = Actor('top')
   bottom_pipe = Actor('bottom')

- Press **play** to see the effct. 
