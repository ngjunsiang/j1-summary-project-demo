"""mud.py

Main module for the game.
"""

import action

def epilogue():
    print("Thanks for playing!")
    print("(Stay tuned for more.)")

def welcome():
    print("TODO: Add welcome message")


class Game:
    def __init__(self):
        pass

    def add_player(self, player):
        """Add player to the game"""
        raise NotImplementedError

    def execute(self, actions: list[action.Action]) -> None:
        """Carry out list of actions"""
        raise NotImplementedError

    def get_options(self) -> list[str]:
        """Return list of player options"""
        options = []
        return options

    def get_actions(self, choice: str) -> list[action.Action]:
        """Return list of actions based on player choice"""
        actions = []
        return actions

    def is_gameover(self) -> bool:
        # TODO: Determine gameover condition
        return False

    def status(self) -> dict:
        """Return game status as a dict"""
        status = {}
        return status
    