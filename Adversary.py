#Adversary class and Methods


class Adversary:
    _ID = 0

    def __init__(self, val=0):
        self.id = self.__class__._ID
        self.__class__._ID += 1
        self.val = val
        self.compromised_nodes = []

    def comromise(self,node_id):
        self.compromised_nodes.append(node_id)