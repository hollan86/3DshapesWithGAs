# Creating Basic 3D-Shapes using a Genetic algorithm

## Introduction
A genetic algorithm(GA) is an optimization technique inspired by natural selection. There are numerous applications of GAs. In this project I attempt to create basic 3D shapes using a GA. To achieve this, I have used positional vectors in spherical coordinates system to represent similarly charged points in space. Then I used a simple fitness function that computes the total between all the point charges. 

<img src="https://latex.codecogs.com/gif.latex?\|\mathbf{r}-\mathbf{r}^\prime\|=\sqrt{r^2&plus;r'^2-2rr'\left[{\sin(\theta)\sin(\theta')}{\cos(\phi-\phi')}&plus;\cos(\theta)\cos(\theta')\right]}" title="\|\mathbf{r}-\mathbf{r}^\prime\|=\sqrt{r^2+r'^2-2rr'\left[{\sin(\theta)\sin(\theta')}{\cos(\phi-\phi')}+\cos(\theta)\cos(\theta')\right]}" />

A genetic algorithm based on the [DEAP](https://github.com/deap/deap) framework is then used to maximize this fitness.
