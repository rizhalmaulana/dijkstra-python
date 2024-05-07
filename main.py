from csv_util import read_csv_to_matrix, read_csv_header
from algoritma import dijkstra, lintasan

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

def fetchAllNodes():
    graph = read_csv_to_matrix('assets/Matrik.csv')
    return graph

def shortestPath(start, end):
    graph = read_csv_to_matrix('assets/Matrik.csv')        
    simpul_dipilih = dijkstra(graph, start)
    
    print("Function shortestPath")
    print(f"Simpul Dipilih: {simpul_dipilih}")
    print("------------------\n")

    return {
        'start': start,
        'end': end,
        'lintasan': lintasan(end, simpul_dipilih[end], simpul_dipilih),
    }
    
def shortestPathtoAllNode():
    start = int(0)
    array = []
        
    graph = read_csv_to_matrix('assets/Matrik.csv')
    node_names = read_csv_header('assets/Matrik.csv')

    simpul_dipilih = dijkstra(graph, start)
    
    for i in range(len(simpul_dipilih)):        
        array.append({
            'node': i,
            'end': node_names[i],
            'lintasan': lintasan(i, simpul_dipilih[i], simpul_dipilih),
        })

    return {
        'data': array,
        'start': start
    }
    
def checkDistanceMap(start, end):
    graph = read_csv_to_matrix('assets/Matrik.csv')
    
    simpul_dipilih = dijkstra(graph, start)
    distance = simpul_dipilih[end][0]

    return {
        'start': start,
        'end': end,
        'distance': distance
    }