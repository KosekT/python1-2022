from random import randint, seed
from collections import defaultdict
import pprint

seed(329)
N_NODES = 10

def gen_graph_DIR_UW(edges, always=True):
    res = []
    
    if always == True:
        for x in range(1, N_NODES+1):
            y = randint(1, N_NODES)
            while y == x:
                y = randint(1, N_NODES)
            res.append((x,y))
            
    while len(res) < edges:
        x, y = randint(1, N_NODES), randint(1, N_NODES)
        if x != y and (x, y) not in res:
            res.append((x, y))
            
    show_graph (sorted(res))
    return sorted(res)

def gen_graph_DIR_UW_alt(edges, always=True):
    res = defaultdict(set)
    il = 0
    
    if always == True:
        for x in range(1, N_NODES+1):
            y = randint(1, N_NODES)
            while y == x:
                y = randint(1, N_NODES)
            res[x].add(y)
            il += 1
            
    while il < edges:
            x, y = randint(1, N_NODES), randint(1, N_NODES)
            while y == x:
                y = randint(1, N_NODES)
            res[x].add(y)
            il += 1
            
    # show_graph (sorted(res))
    pprint.pprint (res)
    return sorted(res)

def gen_graph_DIR_UW(edges, always=True):
    res = []
    
    if always == True:
        for x in range(1, N_NODES+1):
            y = randint(1, N_NODES)
            while y == x:
                y = randint(1, N_NODES)
            res.append((x,y))
            
    while len(res) < edges:
        x, y = randint(1, N_NODES), randint(1, N_NODES)
        if x != y and (x, y) not in res:
            res.append((x, y))
            
    show_graph (sorted(res))
    return sorted(res)

def show_graph(graph):
    print ("------ START ------")
    prev = 0
    for edges in graph:
        if prev != edges[0]:
            print ()
            prev = edges[0]
        print (edges, end='')
    print ("\n------- END -------")

def adjacency_matrix(graph):
    matrix = []
    for x in range(1, N_NODES+1):
        for y in range(1, N_NODES+1):
            x + y
            
    return matrix

def matrix_into_graph(matrix, w=False):
    return

def edges_into_graph(matrix, w=False, d=True):
    return

def set_nodes(n):
    N_NODES = n