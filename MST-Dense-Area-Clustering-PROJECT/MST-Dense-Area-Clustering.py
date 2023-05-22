# Yassine Nader Serrid 2181156439
# Rami Mohammed Saleh 2161122487
# Final Project
import random

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import deque as queue
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=np.inf)

shape = None
while True:
    try:
        shape = int(input("Enter the shape of the 2D array :"))
        break
    except ValueError:
        print('Please input an integer value ...')
print("-----------------------")
#-------------------------------------------------#
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]


# Returns true if mat[N][N] is symmetric, else false
def isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
#-------------------------------------------------#
# make N*N matrix and initialize it will all value as false
visited = [[False for i in range(shape)] for j in range(shape)]


# function which visits all node using BFS algorithm
def matrixbfs(mat):
    # define queue
    q = queue()

    # Mark the starting cell as visited
    # and push it into the queue

    # find the first cell whose value as 1 and start BFS algorithm from that node
    starti = 0
    startj = 0
    flag = 0
    for i in range(0, shape):
        for j in range(0, shape):
            if (mat[i][j] == 1):
                starti = i
                startj = j
                # if we found first 1 then make flag 1 and break the loop
                flag = 1
                break
            if flag == 1:
                break

    # append first node in queue
    q.append((starti, startj))
    # make it visited
    visited[starti][startj] = True

    # iterate loop until all reachable nodes are not visited
    while len(q) > 0:
        # pop front from queue
        current = q.popleft()

        x = current[0]
        y = current[1]

        # to visit above node of current node
        # check for negative value of index which is for 1st row
        if (x - 1 >= 0) and (mat[x - 1][y] == 1 and visited[x - 1][y] == False):
            # print(x-1," ",y)
            q.append((x - 1, y))
            visited[x - 1][y] = True

        # to visit left side node of current node
        # check for negative value of index which is for 1st column
        if (y - 1 >= 0) and (mat[x][y - 1] == 1 and visited[x][y - 1] == False):
            # print(x," ",y-1)
            q.append((x, y - 1))
            visited[x][y - 1] = True

        # to visit below  node of current node
        # check for index out of bound for last row
        if (y + 1 < shape) and (mat[x][y + 1] == 1 and visited[x][y + 1] == False):
            # print(x," ",y+1)
            q.append((x, y + 1))
            visited[x][y + 1] = True

        # to visit right side node of current node
        # check for index out of bound for last column
        if (x + 1 < shape) and (mat[x + 1][y] == 1 and visited[x + 1][y] == False):
            # print(x+1," ",y)
            q.append((x + 1, y))
            visited[x + 1][y] = True
#-------------------------------------------------#
base = np.zeros((shape,shape))
for _ in range(400):
    a = np.random.randint(shape)
    b = np.random.randint(shape)
    if a != b:
        base[a, b] = 1
        base[b, a] = 1
print("The Output Of The Original Matrix:")
print(base)
mat = base
if (isSymmetric(mat, 3)):
    print("Yes, It's Symmetric")
else:
    print("No, It's Not Symmetric")
print("-----------------------")
#-------------------------------------------------#
# Fetch the location of the 1s.
Weightofedges = base
ones = np.argwhere(Weightofedges == 1)
ones = ones[ones[:, 0] < ones[:, 1], :]

# Assign random values.
for a, b in ones:
    Weightofedges[a, b] = Weightofedges[b, a] = np.random.randint(100)
print("The Output Of The Weight Of Edges:")
print(Weightofedges)
mat = Weightofedges
if (isSymmetric(mat, 3)):
    print("Yes, It's Symmetric")
else:
    print("No, It's Not Symmetric")
matrixbfs(mat)
# print visited matrix
for i in range(shape):
    for j in range(shape):
        print(visited[i][j], end=" ")
    print()
print()

# check matrix is connected or not using visited matrix
isconnected = True
for i in range(shape):
    for j in range(shape):
        if mat[i][j] == 1 and visited[i][j] == False:
            isconnected = False
            break

# print result
if isconnected == True:
    print("Matrix is connected")
else:
    print("Matrix is not connected")
print("-----------------------")
#-------------------------------------------------#
from scipy.sparse.csgraph import minimum_spanning_tree
X = minimum_spanning_tree(Weightofedges)
print("The Output Of The MST By Kruskal Algorithm:")
print("  Edges:    Weights:")
print(X)
print("-----------------------")
my_matrix3 = X.toarray().astype(int)
print('The Output Of Directed MST Array:')
print(my_matrix3)
print("-----------------------")
print('The Output Of Undirected MST Array:')
UnDirectedGraph = my_matrix3 + my_matrix3.T - np.diag(np.diag(my_matrix3))
print(UnDirectedGraph)
print('The Total Weight (Cost) Of MST:')
WeightCostMST = np.sum(my_matrix3)
print(WeightCostMST)
print('The Total Weight (Cost) Of Weight Of Edges Matrix:')
WeightCostEdge = np.sum(Weightofedges)/2
print(WeightCostEdge)
print("-----------------------")

#-------------------------------------------------#
A = UnDirectedGraph
G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.Graph)
print("The Degree Of All Nodes For The MST:")
print("(Node,Degree Of The Node(the number of connections that it has to other nodes in the network))")
for i in G.degree():
    print(list(i))

print("-----------------------")
clusters = {}
for i in range(shape):
    print('The Neighbors of node', i, 'Are:')
    print(list(nx.all_neighbors(G, i)))
    clusters[i] = list(nx.all_neighbors(G, i))

nodes_order = sorted(clusters.keys(), key=lambda node: len(clusters[node]), reverse=True)

mst = []
while len(nodes_order) > 0:
    highest_node = nodes_order.pop(0)
    highest_cluster_neighbors = clusters[highest_node]
    del clusters[highest_node]
    for neighbor in highest_cluster_neighbors:
        del clusters[neighbor]
        for root in clusters:
            if neighbor in clusters[root]:
                clusters[root].remove(neighbor)
    highest_cluster_neighbors.append(highest_node)
    mst.append(sorted(highest_cluster_neighbors))
    nodes_order = sorted(clusters.keys(), key=lambda node: len(clusters[node]), reverse=True)
print("-----------------------")
print("Number Of Nodes = ", G.number_of_nodes())
print("Number Of Edges = ", G.number_of_edges())
print("The Ratio Between The Cost of MST Over The Cost Of Weighted Edges Matrix =", WeightCostMST/WeightCostEdge)
print("-----------------------")

colors = ["#" + ''.join([random.choice('C12EF56AB9780D34') for j in range(6)]) for i in range(len(mst))]
clusters = []
for cluster, color in zip(mst, colors):
    clusters.append({'nodes': cluster, 'color': color})

color_map = []
for i in range(shape):
    found = False
    for cluster in clusters:
        for node in cluster['nodes']:
            if node == i:
                color_map.append(cluster['color'])
                found = True
                break
        if found:
            break


plt.figure(1)
A = UnDirectedGraph
G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.Graph)
layout = nx.spring_layout(G)
nx.draw(G, layout, node_color=color_map, with_labels=1)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

plt.figure(2)
A = Weightofedges
G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.Graph)
nx.draw(G, layout,with_labels=1)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

plt.figure(3)
A = UnDirectedGraph
G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.Graph)
nx.draw(G, layout, with_labels=1)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
plt.show()
#-------------------------------------------------#
