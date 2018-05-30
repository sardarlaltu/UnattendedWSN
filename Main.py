# program to check performance of the algorithms
from Sensor import Sensor
from Sink import Sink
from Adversary import Adversary

from Data import *
from Node import Node
import random
from Storage import Storage
import matplotlib.pyplot as plt

#Global variables
N_max = 1000    # no of nodes in the network, global variable
t = 3       #
n = 5       #
m = 3       #
n_s = 50
noOfRounds = 20
interval = 5


def generate_data():
    print ("data Generation")



def sensing_node():

    print("Sensing Node Algo")


def sending_node():
    print("Sensing Node Algo")


def store_node():
    a=0


def sink_data_collection():
    a=0


def sink_data_authentication():
    a=0


#############################  MAIN PART ###################################
#for round in range(noOfRounds):
#    generate_data()
'''
generate_nodes(N_max)

print (nodeList.__len__(), nodeList[5].id )

l = []
for i in range(5):
    temp_share = DataShare(i*11 %13, (i*7)%5, i)
    dataShareList.append(temp_share)

    l.append(temp_share)

for i in range(l.__len__()):
    print("\n")
    # l[i].show_share()

for i in range(l.__len__()):
    print("\n")
    #l[i].show_share()

'''
# ==================   MAIN code HERE   =================================

#for i in range(N_max):
    #print(i, "-> ",arr[i])

#------------------- Adversarial Deletion ----------------------------

for n in [5,4]:
    for m in [3,3]:
        print("Ongoing -> n = " +str(n) +" m = "+str(m))
        f = open("result", "a+")
        f.write("N = "+str(N_max)+" m = "+str( m)+" n = "+str(n) +" t = "+str(t)+ " n_s = "+str(n_s)+"\n")
        f.close()

        print(N_max, m, noOfRounds, N_max * m * noOfRounds)
        l = []

        for n_a in range( interval, n_s+1 ,interval):
            print(n_a)

            n_dashed = []
            dataList = []
            dataShareList = []
            secretKeyList = []
            secretShareList = []
            hashKeyList = []
            nodeList = []
            macDataList = []


            def generate_nodes(N_max):
                for i in range(N_max):
                    temp_node = Node()
                    temp_node.generate_data_storage(noOfRounds)
                    nodeList.append(temp_node)
                return


            def select_nodes_dc(N, m):
                node_ids = []
                for i in range(m):
                    r = random.randint(0, N - 1)
                    if r not in node_ids:
                        node_ids.append(r)
                return node_ids


            def select_nodes_ks(N, m):
                node_ids = []
                for i in range(m):
                    r = random.randint(0, N - 1)
                    if r not in node_ids:
                        node_ids.append(r)
                return node_ids


            # ----------------------------- Sending Node -----------------------------
            generate_nodes(N_max)

            for r in range(noOfRounds):  # for each rounds
                for j in range(N_max):  # for each node
                    node = nodeList[j]

                    data = Data(r, j)
                    node.data_storage.append(data.id)

                    mac_data = Data(r, j)
                    mac_data.changed_to_mac(data.id)

                    sk = SecretKey(r, j, data.id)
                    data.encrypt()
                    data.change_secret_key_id(sk.id)
                    SK = []
                    for l in range(n):
                        key_share = SecretShare(r, j, l)
                        secretShareList.append(key_share)
                        SK.append(key_share)
                    sk.shares = SK
                    # ----------------------------- Sending Node -----------------------------
                    data.destination = select_nodes_dc(N_max, m)  # DC
                    sk.destination = select_nodes_ks(N_max, n)  # KS

                    data.delete()

                    dataList.append(data)
                    macDataList.append(mac_data)
                    secretKeyList.append(sk)

            # ----------------------------- Store Node -----------------------------
            # print("Hello World Testing")
            # print(dataList.__len__())
            # print(Data._ID)

            for r in range(noOfRounds):  # for each rounds
                for j in range(N_max):  # for each node
                    node = nodeList[j]
                    K = HashKey(r, j)
                    XK = []
                    SKA = []
                    XC = []
                    CA = []
                    p = 0
                    q = 0

                    for i in range(dataList.__len__()):
                        data = dataList[i]
                        # print("My checkup")
                        # print (data.show())
                        if j in data.destination:
                            XC.append(i)
                            CA.append(data.id)
                    for i in range(secretShareList.__len__()):
                        sk = secretShareList[i]
                        if j == sk.source_node_id:
                            XK.append(sk)
                            SKA.append(sk)
            # ---------- Data Checkup -------------
            arr = list(range(N_max))

            for i in range(N_max):
                arr[i] = 0

            for i in range(dataList.__len__()):
                data = dataList[i]
                dt = data.destination
                for j in range(dt.__len__()):
                    arr[dt[j]] += 1

            n_dashed = set([])
            k = 0
            for round in range(noOfRounds):
                compromised_nodes = select_nodes_dc(N_max,n_a)
                initialized_nodes = list(range(round*n_s, (round+1)*n_s))
                for a in compromised_nodes:
                    n_dashed.add(a)

                for a in initialized_nodes :
                    if a in n_dashed:
                        n_dashed.remove(a)

                # -----------------  SINK NODE DATA COLLECTION ------------------

                #k += n_dashed.__len__()
                for i in range (dataList.__len__()):
                    data = dataList[i]

                    if data.round< round:
                        data.destination = list(set(data.destination) - set(n_dashed))

                    sk = secretKeyList[i]
                    if sk.round <round:
                        sk.destination = list(set(sk.destination) - set(n_dashed))

            for i in range(dataList.__len__()):
                if ((dataList[i].destination).__len__() >0) and ((secretKeyList[i].destination).__len__() > t-1):
                    k += 1

            print( k)

            f = open("result", "a+")
            f.write(str(n_a)+" ")
            f.write(str(k)+"\n")
            f.close()
            # -----------------  SINK NODE DATA AUTHENTICATION ------------------
        print("The End -> n = " + str(n) + " m = " + str(m))

print("Successfully Program Terminated")
