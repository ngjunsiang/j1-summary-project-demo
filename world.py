"""room.py

Classes representing locations in the game.
"""

def flip(direction: str) -> str:
    """Flip a direction"""
    direction = direction.upper()
    flipped = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E"
    }
    if direction not in flipped:
        raise ValueError(f"Invalid direction: {direction}")
    return flipped[direction]


class Room:
    """Encapsulates room data and contents."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exit: dict[str, str | None] = {
            "N": None,
            "S": None,
            "E": None,
            "W": None
        }
        self._contents = []
        self._characters = []

    def get_exit(self, direction: str) -> str | None:
        """Return room name in given direction"""
        return self.exit[direction]

    def set_exit(self, direction: str, room: str) -> None:
        """Set exit to room in given direction"""
        self.exit[direction] = room

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

    def pop_character(self, name: str):
        """Remove character from room"""
        for character in self._characters:
            if character.name == name:
                self._characters.remove(character)
                return character

    def put_character(self, character) -> None:
        """Add character to room"""
        self._characters.append(character)

    def put_item(self, item) -> None:
        """Add item to room contents"""
        self._contents.append(item)

    def remove_item(self, item):
        """Removes item from room"""
        self._contents.remove(item)


class World:
    """Represents a collection of interconnected rooms"""
    def __init__(self):
        # Refer to rooms by name
        self.rooms = {}

    def add_room(self, room: Room) -> None:
        """Add room to world"""
        self.rooms[room.name] = room

    def get(self, name: str) -> Room:
        """Return room with matching name"""
        return self.rooms[name]

    def join_rooms(self, room1: str, room2: str, direction: str):
        """Connect two rooms in a given direction.
        E.g. join_rooms("A", "B", "N") connects room B so that
        it is north of A.
        """
        r1 = self.get(room1)
        r2 = self.get(room2)
        r1.set_exit(direction, r2.name)
        r2.set_exit(flip(direction), r1.name)

