from csv_util import read_csv_to_matrix, read_csv_header
from algoritma import dijkstra, lintasan

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

def fetchAllNodes():
    graf = read_csv_to_matrix('assets/Matrik.csv')
    return graf

def shortestPath(start, end):
    graf = read_csv_to_matrix('assets/Matrik.csv')
    
    simpul_dipilih = dijkstra(graf,start)
    
    return {
        'start': start,
        'end': end,
        'path': lintasan(end, simpul_dipilih[end], simpul_dipilih),
        'distance': simpul_dipilih[end][0]
    }
    
def shortestPathtoAllNode(start):
    graf = read_csv_to_matrix('assets/Matrik.csv')
    node_names = read_csv_header('assets/Matrik.csv')
    
    simpul_dipilih = dijkstra(graf, start)
    array = []

    for i in range(len(simpul_dipilih)):
        arr = list([[0, 1, 23, 24], [1, 2, 23, 24, 0], [2, 3, 4, 9], [3, 4, 5, 2], [4, 8, 9, 3, 2], [5, 6, 7, 3], [6, 7, 5], [7, 8, 6, 5], [8, 9, 7, 4], [9, 10, 8, 4, 2], [10, 11, 12, 9], [11, 12, 10], [12, 13, 14, 11, 10], [13, 15, 17, 12], [14, 15, 12], 
                    [15, 16, 14, 13], [16, 17, 15], [17, 18, 16, 13], [18, 19, 23, 24, 17], [19, 20 ,21, 22, 18], [20, 21, 19], [21, 22, 20, 19], [22, 23, 21, 19], [23, 24, 18, 1, 0], [24, 23, 18, 1, 0]])
        
        resultNan = np.array(simpul_dipilih[i][0])
        resultNan = np.nan_to_num(resultNan, copy=True, posinf=0, neginf=0)
        changeInt = int(resultNan)

        array.append({
            'node': i,
            'end': node_names[i],
            'path': arr[i],
            # 'path': lintasan(i, simpul_dipilih[i], simpul_dipilih),
            'distance': changeInt
        })

    print(f'Array result {array}')

    return {
        'data': array,
        'start': start
    }
   
def add_vertex(v):
    global graph
    global vertices_no
    global vertices

    if v in vertices :
        print(f'Vertex {v} sudah ada.')
    else :
        vertices_no = vertices_no + 1
        vertices.append(v)
        
        if vertices_no > 1 :
            for vertex in graph:
                vertex.append(0)
        temp = []

        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices

    if v1 not in vertices:
        print(f'Vertex {v1} tidak ada.')
    elif v2 not in vertices:
        print(f'Vertex {v2} tidak ada.')
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def printGraph():
    global graph
    global vertices_no

    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(f'{vertices[i]} -> {vertices[j]} => jarak: {graph[i][j]}')


# vertices = []
# vertices_no = 0
# graph = []

# add_vertex("V0"), 
# add_vertex("V1"), 
# add_vertex("V2"),
# add_vertex("V3"), 
# add_vertex("V4"),
# add_vertex("V5"),
# add_vertex("V6"), 
# add_vertex("V7"), 
# add_vertex("V8"),
# add_vertex("V9"), 
# add_vertex("V10"), 
# add_vertex("V11"), 
# add_vertex("V12"),
# add_vertex("V13"), 
# add_vertex("V14"), 
# add_vertex("V15"), 
# add_vertex("V16"), 
# add_vertex("V17"),
# add_vertex("V18"),
# add_vertex("V19"),
# add_vertex("V20"),
# add_vertex("V21"), 
# add_vertex("V22"), 
# add_vertex("V23"),
# add_vertex("V24"),

# add_edge("V0", "V1", 4.31)
# add_edge("V0", "V23", 4.03)
# add_edge("V0", "V24", 2.67)
# add_edge("V1", "V2", 8.41)
# add_edge("V1", "V23", 8.07)
# add_edge("V1", "V24", 8.44)
# add_edge("V2", "V3", 12.43)
# add_edge("V2", "V4", 8.60)
# add_edge("V2", "V9", 13.24)
# add_edge("V3", "V4", 5.26)
# add_edge("V3", "V5", 15.62)
# add_edge("V4", "V8", 9.55)
# add_edge("V4", "V9", 8.90)
# add_edge("V5", "V6", 12.99)
# add_edge("V5", "V7", 8.70)
# add_edge("V6", "V7", 18.73)
# add_edge("V7", "V8", 14.10)
# add_edge("V8", "V23", 6.93)
# add_edge("V9", "V10", 15.86)
# add_edge("V10", "V11", 7.10)
# add_edge("V10", "V12", 8.46)
# add_edge("V11", "V12", 8.25)
# add_edge("V12", "V13", 8.99)
# add_edge("V12", "V14", 7.07)
# add_edge("V13", "V15", 5.07)
# add_edge("V13", "V17", 6.21)
# add_edge("V14", "V15", 5.58)
# add_edge("V15", "V16", 4.15)
# add_edge("V16", "V17", 3.67)
# add_edge("V17", "V18", 5.43)
# add_edge("V18", "V19", 2.54)
# add_edge("V18", "V23", 7.30)
# add_edge("V18", "V24", 7.83)
# add_edge("V19", "V20", 20.13)
# add_edge("V19", "V21", 18.25)
# add_edge("V19", "V22", 13.36)
# add_edge("V20", "V21", 5.19)
# add_edge("V21", "V22", 14.92)
# add_edge("V22", "V23", 6.63)
# add_edge("V23", "V24", 2.59)

# printGraph()
# print(f'Reperesntasi matrik: {graph}')


def sort(graf, type='asc'):
    new_graf = []
    for i in range(len(graf)):
        j = 0
        k = 0
        if len(new_graf) > 0:
            while j < len(new_graf) and graf[i]['distance'] > new_graf[j]['distance']:
                j += 1
                k = j

    new_graf.insert(k, {
        'node': graf[i]['node'],
        'end': graf[i]['end'],
        'path': graf[i]['path'],
        'distance': graf[i]['distance']
        })
    return new_graf

def main():
    pass
 
if __name__ == '__main__':
    main()