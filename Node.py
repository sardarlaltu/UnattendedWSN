from Storage import Storage


class Node:
    _ID = 0

    def __init__(self, val=0,no_of_rounds=20):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.val = val
        self.no_of_rounds = no_of_rounds
        self.present_round_no = -1
        self.data_storage = []

        self.sym_key = 0
        #self.data_store = generate_data_storage()

    def generate_data_storage(self, no_of_rounds):
        no_of_rounds = self.no_of_rounds
        data_storage = []
        for i in range(no_of_rounds):
            temp_storage = Storage(self.id, i)
            data_storage.append(temp_storage)
        return data_storage

    def view_node_data(self,id=-1):
        if id == -1 :
            print (" To view node data give node id\n")
        elif id >=  self.__class__._ID:
            print ("Invalid Node ID\n")
        else:
            print("Node ID = ",self.id)
            print("Present Round",self.present_round_no )

    def show(self):
        print("id =",self.id )
        print("val =", self.val)
        print("no_of_rounds =",self.no_of_rounds )
        print("present_round_no =",self.present_round_no )
        print("data_storage =")
        for i in range(self.data_storage.__len__()):
            print("data_storage =", self.data_storage[i])
