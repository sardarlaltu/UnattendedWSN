

class Data:
    _ID = 0

    def __init__(self, round = -1, source = -1 ):
        self.id = self._ID +1
        self.__class__._ID += 1

        self.encryption = False
        self.round = round
        self.ifDeleted = False
        self.source = source                #id of the source node
        self.destination = []      #destination will ne id of a node
        self.shares = []
        self.mac = False
        self.mac_source_id= None
        self.secret_key_id = None
        self.pub_encryption = False

    def change_destination(self,destination= []):
        if destination == []:
            print("send destination number")
        else:
            self.destination = destination

    def encrypt(self):
        self.encryption = True

    def pub_encrypt(self):
        self.pub_encryption = True

    def decrypt(self):
        self.encryption = False

    def generate_shares(self, n, type):
        shares = []
        if type == "data":
            for i in range(n):
                temp_share = DataShare(self.id, self.round, i)
                shares.append(temp_share)
        if type == "secret":
            for i in range(n):
                temp_share = SecretShare(self.id, self.round, i)
                shares.append(temp_share)
        self.shares = shares
        return self

    def changed_to_mac(self, data_id):
        self.mac = True
        self.mac_source_id= data_id

    def change_secret_key_id(self, id):
        self.secret_key_id = id

    def show(self):
        print ("encryption ->", self.encryption)
        print("round ->", self.round)
        print("deleted ->", self.ifDeleted)
        print("source ->", self.source)                #id of the source node
        print("destination ->", self.destination)      #destination will ne id of a node
        print("shares ->", self.shares)
        print("mac ->", self.mac)

    def delete(self):
        self.ifDeleted = True

class DataShare:
    _ID = 0

    def __init__(self, round ,source_node_id, share_no):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.source_node_id = source_node_id
        self.round = round
        self.share_no = share_no

    def show_share(self):
        print ("id= ",self.id)
        print("source_node_id= ", self.source_node_id)
        print("round ", self.round)
        print("share_no", self.share_no)

    def show(self):
        print("id  = ",self.id )
        print("source_node_id  = ",self.source_node_id )
        print("round  = ",self.round )
        print("share_no  = ", self.share_no )


class SecretKey:
    _ID = 0

    def __init__(self,  round =-1 , source=-1, data_id=-1 ):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.round = round
        self.data_id = data_id
        self.ifDeleted = False
        self.share = []
        self.source = source  # id of the source node
        self.destination = -1  # destination will ne id of a node

    def set_destination(self, destn_id):
        self.destination = destn_id

    def delete(self):
        self.ifDeleted = True

    def show(self):
        print("id  = ", )
        print("self.round  = ",self.round )
        print("self.data_id  = ", self.data_id )
        print("self.ifDeleted  = ",self.ifDeleted )
        for i in range (self.share.__len__()):
            print(self.share[i])
        print(" self.source= ",self.source )
        print("self.destination", self.destination )


class SecretShare:
    _ID = 0

    def __init__(self, round, source_node_id  ,share_no):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.source_node_id = source_node_id
        self.round = round
        self.share_no = share_no

    def show_share(self):
        print ("id= ",self.id)
        print("source_node_id= ", self.source_node_id)
        print("round ", self.round)
        print("share_no", self.share_no)

    def show(self):
        print("id  = ", self.id)
        print(" self.source_node_id = ",self.source_node_id )
        print(" self.round = ",self.round )
        print(" self.share_no = ",self.share_no )


class HashKey:
    _ID = 0

    def __init__(self, round, source_node_id  ):
        self.id = self.__class__._ID
        self.__class__._ID += 1

        self.round = round
        self.source = source_node_id

    def show(self):
        print("id = ", self.id)
        print("round = ", self.round)
        print("Source = ", self.source)