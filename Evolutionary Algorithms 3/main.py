from Ant.ACO import ACO
from Ant.readToFile import readFile


def main():
    params = readFile("Data/berlin52.txt")

    probParams = {"noAnts": 100, "generations": 100, "dynamic": 10}
    params['pheromone'] = []
    params['oldPheromoneRate'] = 0.5
    params['q0'] = 0.01
    params['alpha'] = 5
    params['beta'] = 3

    aco = ACO(params, probParams)
    aco.initialize()
    aco.initializePheromone()

    bestOfBestAnt = None

    result = ""
    for i in range(1, probParams['generations']):
        aco.explore()
        bestAnt = aco.bestAnt()
        print("Generation " + str(i) + " best ant distance: " + str(bestAnt.distance()) + " | road: " + str(bestAnt.path()))

        if bestOfBestAnt is None or bestAnt.distance() < bestOfBestAnt.distance():
            bestOfBestAnt = bestAnt

        if i % probParams['dynamic'] == 0:
            aco.deleteEdge()

        f = open("Data/output.txt", "w")
        result = result + str(bestAnt.distance()) + "\n"
        f.write(str(result))
        f.close()

        aco.initialize()

    print("\nCea mai inteligenta furnicuta: " + str(bestOfBestAnt.distance()) + " with path " + str(bestOfBestAnt.path()))


main()
# Best berlin: 7855.8677
# Optimal berlin: 7544.3659
