# evolutionary-algorithms
Python project that contains 3 folders with applications that solve problems using evolutionary algorithms.

<u>The problem of identifying communities in a complex network</u>

Discovering and analyzing communities in networks is a widely debated topic in sociology, biology, and computer science. Complex networks represent the support for different real systems (immune system, brain, transport infrastructure, etc.). A community in these networks is defined as a group of nodes densely connected to each other but loosely connected to nodes in other communities. The application identifies existing communities in a network. Information on the representation of chromosomes and genetic operators is used. The input data is saved in gml files and the output data are saved in txt files (Data package).

The input data are represented by:
- the network graph
- the parameters of the evolutionary algorithm.
  
The output data is represented by:
- the number of communities identified in the graph
- belonging to a certain community for each node of the graph/network
- the way of evolution, over the generations, of the fitness of the best chromosome in the population
- the way of evolution, over the generations, of the number of communities united by the best chromosome in the population
  
<b>The shortest path problem</b>

A project manager must arrive at a discussion with a potential client. His agenda is very busy, having a lot of meetings. Being pressed for time, he wants to take the shortest route to the customer's destination. Based on the address he has, the iMap app gives him several routes to reach his destination, each route marked with an estimated travel time. The application finds the shortest route that starts from a location, visits all locations (each location is visited only once, except the start location which is visited exactly 2 times), and returns to the start location. The input and output data are saved in txt files (Data package).

The [Evolutionary Algorithms 1](https://github.com/Iri25/ai-evolalgos-Iri25/tree/master/Evolutionary%20Algorithms%201) folder contains an application that solves the problem of identifying communities in a complex network using an evolutionary algorithm. 

The [Evolutionary Algorithms 2](https://github.com/Iri25/ai-evolalgos-Iri25/tree/master/Evolutionary%20Algorithms%202) folder contains an application that solves the shortest path problem using evolutionary algorithms.

The [Evolutionary Algorithms 3](https://github.com/Iri25/ai-evolalgos-Iri25/tree/master/Evolutionary%20Algorithms%203) folder contains an application that solves the shortest path problem using evolutionary algorithms, Ant Colony Optimisation (ACO) tehnique.
