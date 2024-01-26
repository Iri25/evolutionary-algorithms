from cmath import sqrt


def parser(filename):
    f = open(filename, "r")
    net = {}
    coords = []
    _ = f.readline()
    _ = f.readline()
    _ = f.readline()
    x = f.readline()

    if filename == "Data/berlin52.txt":
        _, _, dim = x.split()
    else:
        _, dim = x.split()
    net['noNodes'] = int(dim)

    x = f.readline()
    x = f.readline()
    x = f.readline()

    while x != "EOF":
        _, coordx, coordy = x.split()
        coords.append([float(coordx), float(coordy)])
        x = f.readline()

    mat = []
    for i in range(net['noNodes']):
        mat.append([])
        for j in range(net['noNodes']):
            if i == j:
                mat[i].append(0)
                continue
            x1 = coords[i][0]
            x2 = coords[j][0]
            y1 = coords[i][1]
            y2 = coords[j][1]
            mat[i].append(int(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)).real))

    net['noNodes'] = net['noNodes'] - 1
    net['mat'] = mat
    f.close()
    return net


def readFile(filename):
    if filename == "Data/berlin52.txt":
        return parser(filename)
    f = open(filename, "r")
    net = {}
    x = f.readline()
    net['noNodes'] = int(x)-1
    mat = []
    for i in range(net['noNodes']+1):
        mat.append([])
        for j in f.readline().strip().split(","):
            mat[i].append(int(j))
    net['mat'] = mat
    f.close()
    return net


param = readFile("Data/fricker26.txt")


def function(lista):
    cost = 0
    prev = 0
    for el in lista:
        cost = cost + param['mat'][prev][el]
        prev = el
    return cost + param['mat'][prev][0]