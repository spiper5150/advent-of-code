class Submarine:
    def __init__(self, depth = 0, position = 0, aim = 0):
        self.__depth = depth
        self.__position = position
        self.__aim = aim

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, value):
        self.__depth = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def aim(self):
        return self.__aim

    @aim.setter
    def aim(self, value):
        self.__aim = value

    @property
    def coordinates(self):
        return self.__depth * self.__position