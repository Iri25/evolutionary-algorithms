import networkx as nx


def readFile(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if mat[i][j] == 1:
                d += 1
            if j > i:
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


def readGmlFile(fileName):
    if fileName == "krebs.gml":
        graph = nx.read_gml(fileName, label='id')
    else:
        graph = nx.read_gml(fileName)

    net = {'noNodes': graph.number_of_nodes(), 'noEdges': graph.number_of_edges()}

    mat = []
    mat = nx.to_numpy_matrix(graph)
    net["mat"] = mat

    degrees = []
    noEdges = 0
    for i in range(net['noNodes']):
        d = 0
        for j in range(net['noNodes']):
            if mat.item((i, j)) == 1:
                d += 1
            if j > i:
                noEdges += mat.item((i, j))
        degrees.append(d)
    net["degrees"] = degrees

    return net








