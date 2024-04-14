
import sys

if sys.version_info <= (3,):
    raise RuntimeError('Alas, Adventure requires Python 3 or later')

def load_advent_dat(data):
    import os
    from .data import parse

    datapath = os.path.join(os.path.dirname(__file__), 'advent.dat')
    with open(datapath, 'r', encoding='ascii') as datafile:
        parse(data, datafile)
def play(seed=None):
    """Turn the Python prompt into an Adventure game."""
    global _game

    from .game import Game
    from .prompt import install_words
    print("Starting game with seed:", seed)
    _game = Game(seed)
    load_advent_dat(_game)
    install_words(_game)
    _game.start()
    output = _game.output[:-1]
    print("Output from game:", output)  # Print the output
    return output  # Return the game output


def output(game):
    """Return the current output of the game."""
    return game

def resume(savefile, quiet=False):
    global _game

    from .game import Game
    from .prompt import install_words

    _game = Game.resume(savefile)
    install_words(_game)
    if not quiet:
        print('GAME RESTORED\n')
