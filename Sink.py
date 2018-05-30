#sink class and Methods


class Sink:
    _ID = 0

    def __init__(self, val=0):
        self.id = self.__class__._ID
        self.__class__._ID += 1
        self.val = val

