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
    simpul_dipilih = dijkstra(graf, start)
    
    print("Function shortestPath")
    print(f"Simpul Dipilih: {simpul_dipilih}")
    print("-------------\n")

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
        distance = int(simpul_dipilih[i][0]) if not np.isnan(simpul_dipilih[i][0]) else 0
        
        array.append({
            'node': i,
            'end': node_names[i],
            'lintasan': lintasan(i, simpul_dipilih[i], simpul_dipilih),
            'distance': distance
        })

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