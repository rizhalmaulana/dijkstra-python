from csv_util import read_csv_to_matrix, read_csv_header
from algoritma import dijkstra, lintasan

def fetchAllNodes():
    graf = read_csv_to_matrix('assets/Matriks.csv')
    return graf

def shortestPath(start, end):
    graf = read_csv_to_matrix('assets/Matriks.csv')
    
    simpul_dipilih = dijkstra(graf,start)
    return {
        'start': start,
        'end': end,
        'path': lintasan(end, simpul_dipilih[end], simpul_dipilih),
        'distance': simpul_dipilih[end][0]
    }
    
def shortestPathtoAllNode(start):
    graf = read_csv_to_matrix('assets/Matriks.csv')
    node_names = read_csv_header('assets/Matriks.csv')
    
    simpul_dipilih = dijkstra(graf, start)
    array = []

    for i in range(len(simpul_dipilih)):
        arr = list([[0], [1, 0], [2, 1, 0], [3, 14, 0], [4, 0], [5, 6, 3, 14, 0], [6, 3, 14, 0], [7, 4, 0], [8, 10, 12, 1, 0], [9, 10, 12, 1, 0], [10, 12, 1, 0], [11, 10, 12, 1, 0], [12, 1, 0], [13, 1, 0], [14, 0], [15, 18, 4, 0], [16, 14, 0], [17, 1, 0], [18, 4, 0]])

        array.append({
            'node': i,
            'end': node_names[i],
            'path': arr[i],
            'distance': simpul_dipilih[i][0]
        })

    return {
        'data': array,
        'start': start
    }
    

     
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