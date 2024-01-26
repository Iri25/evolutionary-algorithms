from random import seed
from collections import Counter

from Chromosome.geneticAlgorithm import *
from Chromosome.readToFile import readGmlFile
from Chromosome.realChromosome import Chromosome
from Chromosome.utils import optimumFitness


def main():
    param = readGmlFile("Data/adjnoun.gml")
    MIN = 0
    MAX = param['noNodes']

    seed(1)

    gaParam = {'popSize': 100, 'noGen': 100}
    problParam = {'min': MIN, 'max': MAX, 'function': optimumFitness, 'noNodes': MAX}

    allBestFitnesses = []
    allAvgFitnesses = []
    generations = []

    ga = geneticAlgorithm(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestOfBestChromo = Chromosome(problParam)

    result = ""
    for g in range(gaParam['noGen']):
        allPotentialSolutionsX = [c.repres for c in ga.population]
        allPotentialSolutionsY = [c.fitness for c in ga.population]

        bestSolX = ga.bestChromosome().repres
        bestSolY = ga.bestChromosome().fitness

        allBestFitnesses.append(bestSolY)
        allAvgFitnesses.append(sum(allPotentialSolutionsY) / len(allPotentialSolutionsY))

        generations.append(g)

        # ga.oneGeneration()
        ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        if bestOfBestChromo.fitness < bestChromo.fitness:
            bestOfBestChromo = bestChromo
        print('Generation: ' + str(g) + '; Number of communities: ' + str(
            len(Counter(bestChromo.repres).keys())) + '; is: x = ' + str(bestChromo.repres) + ' fitness = '
              + str(bestChromo.fitness))
        f = open("Data/output.txt", "w")
        result = result + str(bestChromo.fitness) + "\n"
        f.write(str(result))
        f.close()

    print('\n')
    print("Number of communities: " + str(len(Counter(bestOfBestChromo.repres).keys())))
    print("Best solution: " + str(bestOfBestChromo.repres) + '\n')
    print("Best fitness: " + str(bestOfBestChromo.fitness) + '\n')



main()
