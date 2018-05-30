

class Storage:
    _ID = 0

    def __init__(self, node_id = -1 , round =-1):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.round = round
        self.node_id = node_id

        self.XK = []
        self.XC = []
        self.SKA = []
        self.CA = []
        self.HSK = []
        self.HC = []
        self.Z = []


    def show(self):
        print ("Storage is not Visible")
