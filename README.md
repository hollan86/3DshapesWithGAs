# Creating Basic 3D-Shapes using a Genetic algorithm

## Abstract
A genetic algorithm(GA) is an optimization technique inspired by natural selection. There are numerous applications of GAs. In this project I attempt to create basic 3D shapes using a GA. To achieve this, I have used positional vectors in spherical coordinates system to represent similarly charged points in space. Then I used a simple fitness function that computes the total between all the point charges. 

A genetic algorithm based on the [DEAP](https://github.com/deap/deap) framework is then used to maximize this fitness. The genome used in initial experiments is a list containing random charge locations in spherical coordinates. Initial experiments show that it is possible to obtain optimum shapes using this setup. As seen below, if the genome is of length 2, the optimum shape is a straight line connecting the two point charges. If the genome is of length 3, optimum shape is an equilateral triangel connecting the three point charges. If the genome length is 4, the optimal shape is a tetrahedron. Checkout the main notebook for interactive plots.

## Genome length = 2

![](https://github.com/hollan86/3DshapesWithGAs/blob/main/genome2.png)

## Genome length = 3

![](https://github.com/hollan86/3DshapesWithGAs/blob/main/genome3.png)

## Genome length = 4
![](https://github.com/hollan86/3DshapesWithGAs/blob/main/genome4.png)

