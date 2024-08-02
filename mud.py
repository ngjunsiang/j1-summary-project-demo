"""mud.py

Main module for the game.
"""

import action
import world

def epilogue():
    print("Thanks for playing!")
    print("(Stay tuned for more.)")

def welcome():
    print("TODO: Add welcome message")


class Game:
    def __init__(self, spawn_point: str):
        # Start location for added characters
        self.spawn_point = spawn_point
        # Track character locations
        self.locations = {}
        self.world = world.World()

    def add_player(self, player, location: str = ""):
        """Add player to the game"""
        # If location not provided, use spawn point
        location = location or self.spawn_point
        self.locations[player.name] = location

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
    