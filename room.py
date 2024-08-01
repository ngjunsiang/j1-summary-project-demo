"""room.py

Classes representing locations in the game.
"""

class Room:
    """Encapsulates room data and contents."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exit = {
            "N": None,
            "S": None,
            "E": None,
            "W": None
        }
        self._contents = []
        self._characters = []

    def put_item(self, item) -> None:
        """Add item to room contents"""
        self._contents.append(item)

    def get_item_by_name(self, name: str):
        """Returns item with matching name.
        Does not remove item from room.
        """
        for item in self._contents:
            if item.name == name:
                return item

    def list_characters(self) -> list[str]:
        """Return a list of character names"""
        names = []
        for character in self._characters:
            names.append(character.name)
        return names

    def list_items(self) -> list[str]:
        """Return a list of item names"""
        names = []
        for item in self._contents:
            names.append(item.name)
        return names

    def remove_item(self, item):
        """Removes item from room"""
        self._contents.remove(item)

    def put_character(self, character) -> None:
        """Add character to room"""
        self._characters.append(character)

    def pop_character(self, name: str):
        """Remove character from room"""
        for character in self._characters:
            if character.name == name:
                self._characters.remove(character)
                return character

