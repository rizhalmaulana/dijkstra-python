import heapq

def dijkstra(graph, start):
    INFINITY = 1e9
    L = [[INFINITY, None] for _ in range(len(graph))]
    L[start] = [0, None]
    S = []
    
    for _ in range(len(graph)):
        mini = INFINITY
        minind = None
        for j in range(len(graph)):
            if L[j][0] < mini and j not in S:
                mini = L[j][0]
                minind = j
        if minind is None:
            break
        S.append(minind)
        
        for i in range(len(graph)):
            if graph[minind][i] != 0 and i not in S:
                if L[i][0] > L[minind][0] + graph[minind][i]:
                    L[i][0] = L[minind][0] + graph[minind][i]
                    L[i][1] = minind
    return L

def lintasan(akhir, simpul, graf_hasil):
    array_simpul = [akhir]
    current_distance = simpul[0]
    
    print(f"end: {akhir}")
    print(f"simpul awal: {simpul}")
    print("--------------------\n")
            
    while simpul[1] != None:
        next_node = simpul[1]
        next_distance = graf_hasil[next_node][0]  # Jarak dari simpul awal ke simpul berikutnya
        
        if next_distance > current_distance:
            print("Jarak pada simpul berikutnya lebih besar dari jarak sebelumnya.")
        
        array_simpul.append(next_node)
        simpul = graf_hasil[next_node]
        
        current_distance = next_distance  # Update jarak sekarang
        
        print(f"arr simpul: {array_simpul}")
        print(f"simpul akhir: {simpul}")
        print("-------------------\n")
    return array_simpul
