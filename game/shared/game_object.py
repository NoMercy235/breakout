class GameObject:

    def __init__(self, position, size, sprite):
        self._position = position
        self._size = size
        self._sprite = sprite

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size

    def get_sprite(self):
        return self._sprite

    def intersects(self, other):
        pass
