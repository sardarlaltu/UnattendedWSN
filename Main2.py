k=23
l = list (range(100))
f = open("result","a+")
f.write(str(k))
f.write(str(l))
f.close()

k=23
l = list (range(24))
f = open("result","a+")
f.write(str(k))
f.write(str(l))
f.close()

'''
N = 1000      # Total number of nodes
n_s = 50       # no of nodes sink visits in each round

n = 5           # n is of (t,n) scheme
t = 3           # t is of (t,n) scheme
m = 3           # m is the number of replication

n_a = 20        # adversary compromise nodes in each round

v = N/n_s         # no of rounds in which sink visits

no_of_compromised_nodes = 0
no_of_unrecoverable_data = 0


no_of_data_per_round = N * m
no_of_data_total = N * m * v
sink_collects_per_round = n_a * no_of_data_per_round

print("no of nodes N = ",N)
print("no of rounds v = ",v)
print("sink visits per round n_s = ", n_s)

print("no_of_data_per_round = ", no_of_data_per_round)
print("no_of_data_total ", no_of_data_total)
print("sink_collects_per_round", sink_collects_per_round)

print("no of data a node generates per round", m)
print("no of data a node generates v round", v*m)

for no_of_compromised_nodes in range(0, N, 100):

    no_of_compromised_data = no_of_compromised_nodes*m*v
    no_of_uncompromised_data = no_of_data_total - no_of_compromised_data

    #print("no_of_compromised_data",no_of_compromised_data)
    #print("compromised_nodes = ",no_of_compromised_nodes)
    #print("no_of_uncompromised_data",no_of_uncompromised_data)

    # print("no_of_unrecoverable_data",no_of_unrecoverable_data)

    print(no_of_compromised_data,no_of_compromised_nodes,no_of_uncompromised_data)


    print("")
    print("")
    print("")

'''