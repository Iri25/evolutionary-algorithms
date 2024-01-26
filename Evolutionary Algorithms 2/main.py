from random import seed

from Chromosome.GA import *
from Chromosome.readToFile import *



def main():
    MIN = 0
    MAX = param['noNodes']

    seed(9)

    gaParam = {'popSize': 100, 'noGen': 100}
    problParam = {'min': MIN, 'max': MAX, 'function': function, 'noNodes': MAX}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestOfBestChromo = Chromosome(problParam, param['mat'])
    bestOfBestChromo.fitness = 10000000

    result = ""
    for g in range(gaParam['noGen']):

        bestSolX = ga.bestChromosome().repres
        bestSolY = ga.bestChromosome().fitness

        # ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        if bestOfBestChromo.fitness > bestChromo.fitness:
            bestOfBestChromo = bestChromo

        print('Generation: ' + str(g) + '; X: ' + str(bestChromo.repres) + '; fitness = ' + str(bestChromo.fitness))
        f = open("Data/output.txt", "w")
        result = result + str(bestChromo.fitness) + "\n"
        f.write(str(result))
        f.close()
    print('\n')
    print("Best solution: " + str(bestOfBestChromo.repres))
    print("Best fitness: " + str(bestOfBestChromo.fitness))


main()