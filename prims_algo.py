def empty_graph(n):
    adjMatrix = []
    for i in range(n):
        row1 = []
        for j in range(n):
            row1.append(0)
        adjMatrix.append(row1)
    return adjMatrix

def extension(vertices, graph):
    n = len(graph)
    for i in vertices:  #for each connected vertex in graph
        for j in range(n):  #for each vertex in the graph
            if j not in vertices and graph[i][j]:   #find edge {i,j} in graph with i connected and j not
                return i, j

def prims_algo(graph):
    n  = len(graph)
    tree = empty_graph(n)
    conn = [0]
    while len(conn) < n:    #until every vertex in graph is connected
        i, j = extension(conn, graph)
        tree[i][j] = 1
        tree[j][i] = 1
        conn = conn + [j]
    return tree


