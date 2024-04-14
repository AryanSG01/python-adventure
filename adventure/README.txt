
To encourage the use of Python 3, the game is designed to be played
right at the Python prompt.  Single-word commands can be typed by
themselves, but two-word commands should be written as a function call
(since a two-word command would not be valid Python)::

    >>> import adventure
    >>> adventure.play()
    WELCOME TO ADVENTURE!!  WOULD YOU LIKE INSTRUCTIONS?

    >>> no
    YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING.
    AROUND YOU IS A FOREST.  A SMALL STREAM FLOWS OUT OF THE BUILDING AND
    DOWN A GULLY.

    >>> east
    YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A LARGE SPRING.
    THERE ARE SOME KEYS ON THE GROUND HERE.
    THERE IS A SHINY BRASS LAMP NEARBY.
    THERE IS FOOD HERE.
    THERE IS A BOTTLE OF WATER HERE.

    >>> get(lamp)
    OK

    >>> leave
    YOU'RE AT END OF ROAD AGAIN.

    >>> south
    YOU ARE IN A VALLEY IN THE FOREST BESIDE A STREAM TUMBLING ALONG A
    ROCKY BED.

The original Adventure paid attention to only the first five letters of
each command, so a long command like ``inventory`` could simply be typed
as ``inven``.  This package defines a symbol for both versions of every
long word, so you can type the long or short version as you please.

You can save your game at any time by calling the ``save()`` command
with a filename, and then can resume it later::

    >>> save('advent.save')
    GAME SAVED

    >>> adventure.resume('advent.save')
    GAME RESTORED
    >>> look
    SORRY, BUT I AM NOT ALLOWED TO GIVE MORE DETAIL.  I WILL REPEAT THE
    LONG DESCRIPTION OF YOUR LOCATION.
    YOU ARE IN A VALLEY IN THE FOREST BESIDE A STREAM TUMBLING ALONG A
    ROCKY BED.

You can find two complete, working walkthroughs of the game in its
``tests`` directory, which you can run using the ``discover`` module that
comes built-in with Python 3::

    $ python3 -m unittest discover adventure

I wrote most of this package over Christmas vacation 2010, to learn more
about the workings of the game that so enthralled me as a child; the
project also gave me practice writing Python 3.  I still forget the
parentheses when writing ``print()`` if I am not paying attention.

Traditional Mode
================

You can also use this package to play Adventure at a traditional prompt
that does not require its input to be valid Python.  Use your operating
system command line to run the package::

    $ python3 -m adventure
    WELCOME TO ADVENTURE!!  WOULD YOU LIKE INSTRUCTIONS?

    >

At the prompt that will appear, two-word commands can simply be
separated by a space::

    > get lamp
    OK

For extra authenticity, the output of the Adventure game in this mode is
typed to your screen at 1200 baud.  You will note that although this
prints the text faster than you can read it anyway, your experience of
the game will improve considerably, especially when a move results in a
surprise.

Why is the game better at 1200 baud?  When a paragraph of text is
allowed to appear on the screen all at once, your eyes scan the entire
paragraph for important information, often ruining any surprises before
you can then settle down and read it from the beginning.  But at 1200
baud, you wind up reading the text in order as it appears, which unfolds
the narrative sequentially as the author of Adventure intended.

If you created a file with the in-game ``save`` command, you can restore
it later by naming it on the command line::

    > save mygame
    GAME SAVED
    > quit
    DO YOU REALLY WANT TO QUIT NOW?
    > y
    OK

    $ python3 -m adventure mygame
    GAME RESTORED
    >

Notes
=====

* Several Adventure commands conflict with standard Python built-in
  functions.  If you want to run the normal Python function ``exit()``,
  ``open()``, ``quit()``, or ``help()``, then import the ``builtin``
  module and run the copy of the function stored there.

* The word “break” is a Python keyword, so there was no possibility of
  using it in the game.  Instead, use one of the two synonyms defined by
  the PDP version of Adventure: “shatter” or “smash.”



Cave Adventure Walkthrough Summary

Start: You find yourself at the end of a road outside a small brick building. A forest surrounds you, with a stream flowing from the building.

Explore: You can move in various directions, including north, south, east, and west, to explore the surrounding areas. You encounter different environments like valleys, forests, and caves.

Interact: Along the way, you encounter various objects and obstacles. You can interact with these objects by using commands like "get," "drop," or "use" followed by the object's name.

Solve Puzzles: The game involves solving puzzles to progress further. These puzzles may require finding keys, navigating mazes, or unlocking doors.

Discover Treasures: As you explore the cave system, you may discover hidden treasures and valuable items. Collecting these treasures adds to your score and advances your progress in the game.

Encounter Hazards: Be cautious of hazards such as bottomless pits, dangerous creatures, or traps that can harm or hinder your progress.

Navigate: Use a map or mental notes to navigate through the cave system effectively. Some areas may require retracing your steps or finding alternative routes to progress.

Complete Objectives: The ultimate goal of the game is to explore the cave, solve puzzles, and find the legendary Colossal Cave treasure.

Victory: Successfully navigate through the cave, overcome obstacles, and collect the treasure to achieve victory. Your final score reflects your performance in the game.

Here's a list of some common commands or functions used to play the game:

GET: Used to pick up an object from the game world.
DROP: Used to drop or place an object from the player's inventory into the game world.
GO [direction]: Allows the player to move in a specific direction (e.g., north, south, east, west).
LOOK: Provides a description of the current location or examines an object in detail.
INVENTORY or I: Displays a list of items currently held by the player.
SCORE: Shows the player's current score or points earned in the game.
SAVE: Saves the current game progress for later continuation.
RESTORE: Restores a previously saved game state.
QUIT or EXIT: Ends the game session.
KILL: Used to attack or eliminate enemies or obstacles in the game world.
THROW: Allows the player to throw an object in a specified direction or at a target.
OPEN: Used to open doors, containers, or other objects that may be closed or locked.
CLOSE: Opposite of OPEN, used to close doors or containers that are currently open.
READ: Allows the player to read text written on objects or in books found within the game world.
EAT: Used to consume food items found in the game world to restore health or satisfy hunger.
DRINK: Allows the player to consume liquids, such as water or potions.
WEAR: Used to wear or equip clothing or items that can be worn by the player character.
SEARCH: Allows the player to search the current location for hidden items or clues.
LISTEN: Enables the player to listen for sounds or clues in the environment.
CLIMB: Used to climb up or down objects or surfaces within the game world.
ENTER: Allows the player to enter specific locations, such as buildings or caves.

Here's a list of some common places and rooms that players may encounter:

End of Road: The starting location of the game, situated at the end of a road outside a small brick building.
Valley: A low area surrounded by hills or mountains, often containing vegetation and streams.
Forest: A dense area filled with trees, undergrowth, and wildlife.
Stream: A body of flowing water, typically found in valleys or forests.
Building: A structure made of brick or stone, possibly serving as a shelter or storage area.
Well House: A building constructed over a well or water source, often containing valuable items.
Inside Building: The interior of a building, where players may find keys, lamps, food, and other objects.
Cave Entrance: The opening or entrance to the cave system, leading to deeper underground passages.
Dark Cave: A section of the cave system devoid of light, requiring the use of a lamp or light source to navigate.
Maze of Twisty Passages: A complex network of interconnected tunnels and passages, often confusing to navigate.
Round Room: A circular chamber within the cave system, possibly containing hidden treasures or puzzles.
Dragon's Lair: A dangerous area inhabited by a fierce dragon, posing a significant threat to players.
Y2: A mysterious location within the cave system, often associated with puzzles or secrets.
Shell Room: A room containing ancient fossilized shells or other geological formations.
Bedquilt: A chamber with intricate patterns on the walls, resembling a quilt.


Game feature
Exploration: Players can explore a vast and immersive cave system filled with diverse environments, including valleys, forests, and underground chambers.

Puzzles: The game offers a variety of puzzles and challenges for players to solve, ranging from simple object interactions to complex logic puzzles.

Interactive Storytelling: "Colossal Cave Adventure" features an engaging narrative that unfolds as players progress through the game, uncovering secrets and mysteries hidden within the cave.

Inventory Management: Players can collect and manage a variety of items found throughout the cave, using them to solve puzzles, overcome obstacles, and progress in the game.

Dynamic Environment: The cave environment is dynamic and responsive, with changing conditions, hazards, and events that impact gameplay and exploration.

Creatures and Enemies: Players may encounter dangerous creatures and enemies lurking within the cave, requiring strategic thinking and resource management to overcome.

Multiple Endings: The game offers multiple possible outcomes based on the player's actions and decisions, providing replay value and encouraging exploration of different paths.

Atmospheric Sound Design: Immersive sound effects and ambient music enhance the atmosphere of the cave environment, adding to the player's sense of immersion and adventure.

Visual Enhancements: Optional visual enhancements, such as graphical overlays or atmospheric effects, enhance the visual presentation of the game while preserving its classic text-based gameplay.

Modding and Customization: The game may support modding or customization options, allowing players to create and share their own content, levels, or modifications.

Achievements and Progression: Players can earn achievements and track their progress as they explore the cave, solve puzzles, and uncover hidden treasures.

Accessibility Features: The game includes accessibility features to ensure that players of all abilities can enjoy the experience, such as customizable text size, color schemes, and input options.